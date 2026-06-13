from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os

load_dotenv()

# -------------------------------
# GLOBAL VARIABLES
# -------------------------------
vectorstore = None
retriever = None
llm = None  # ← initialized lazily, NOT at module level

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCUMENT_PATH = os.path.join(BASE_DIR, "documents")


def get_llm():
    """Initialize LLM only when first needed — after env vars are loaded."""
    global llm
    if llm is None:
        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.7
        )
    return llm


# -------------------------------
# BUILD VECTORSTORE
# -------------------------------
def build_vectorstore():
    global retriever, vectorstore

    print("🔄 Rebuilding Vector DB...")

    pdf_loader = DirectoryLoader(
        path=DOCUMENT_PATH,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )

    txt_loader = DirectoryLoader(
        path=DOCUMENT_PATH,
        glob="*.txt",
        loader_cls=TextLoader
    )

    pdf_docs = list(pdf_loader.lazy_load())
    txt_docs = list(txt_loader.lazy_load())

    print(f"PDF count: {len(pdf_docs)}, TXT count: {len(txt_docs)}")

    docs = pdf_docs + txt_docs

    if not docs:
        print("⚠️ No documents found!")
        retriever = None
        return

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=30
    )
    splitted_docs = splitter.split_documents(docs)

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
        documents=splitted_docs,
        embedding=embedding_model,
    )

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 3, "lambda_mult": 0.7}
    )

    print("✅ Vector DB Ready!")


# -------------------------------
# Utility: Format Docs
# -------------------------------
def format_docs(docs):
    context = "\n".join([doc.page_content for doc in docs])
    sources = list(set([
        os.path.basename(doc.metadata.get("source", "unknown"))
        for doc in docs
    ]))
    return context, sources


# -------------------------------
# Corrective RAG
# -------------------------------
def corrective_rag(query):
    global retriever

    if retriever is None:
        return "No documents available. Please upload files first.", []

    model = get_llm()

    print("\n🔍 Initial Retrieval")
    retrieved_docs = retriever.invoke(query)
    context, sources = format_docs(retrieved_docs)

    # Relevance Check
    evaluation_prompt = f"""
    Query: {query}

    Retrieved Context:
    {context}

    Are these documents relevant enough to answer the query?
    Respond strictly with YES or NO.
    """
    evaluation = model.invoke(evaluation_prompt).content.strip()
    print("Relevance Check:", evaluation)

    # Query Rewrite if needed
    if "NO" in evaluation.upper():
        print("✏️ Rewriting Query...")
        rewrite_prompt = f"""
        The query '{query}' did not retrieve relevant documents.
        Rewrite it to improve retrieval quality.
        Only return the improved query.
        """
        improved_query = model.invoke(rewrite_prompt).content.strip()
        print("Improved Query:", improved_query)

        retrieved_docs = retriever.invoke(improved_query)
        context, sources = format_docs(retrieved_docs)

    # Final Answer
    final_prompt = f"""
    Answer the question using ONLY the context below.

    Context:
    {context}

    Question: {query}

    Also mention the sources used at the end.
    """
    answer = model.invoke(final_prompt)
    return answer.content, sources


# -------------------------------
# Public Function (used by UI)
# -------------------------------
def get_answer(query: str):
    global retriever

    if retriever is None:
        build_vectorstore()

    if retriever is None:
        return "No documents found. Please upload documents first.", []

    return corrective_rag(query)