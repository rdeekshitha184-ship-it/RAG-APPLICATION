# import reflex as rx
# from DOCU_AI.components.navbar import navbar
# from DOCU_AI.components.footer import footer

# def about():
#     return rx.box(
#         navbar(),

#         rx.box(
#             rx.vstack(
#                 rx.heading("🧠 About DocuAI", size="7"),

#                 rx.text(
#                     "DocuAI is an AI-powered document intelligence system that allows users "
#                     "to upload and interact with documents using natural language queries. "
#                     "It uses Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers."
#                 ),

#                 rx.heading("⚙️ Key Features", size="5"),
#                 rx.text("• Upload and process PDF, TXT, files"),
#                 rx.text("• Ask questions in natural language"),
#                 rx.text("• Context-aware AI responses"),
#                 rx.text("• Confidence score and source tracking"),
#                 rx.text("• Chat history for conversation flow"),

#                 rx.heading("🏗️ System Architecture", size="5"),
#                 rx.text("1. Document Upload"),
#                 rx.text("2. Text Extraction & Processing"),
#                 rx.text("3. Chunking using text splitters"),
#                 rx.text("4. Embedding generation"),
#                 rx.text("5. Vector storage (ChromaDB)"),
#                 rx.text("6. Similarity-based retrieval"),
#                 rx.text("7. Answer generation using LLM"),

#                 rx.heading("🧪 Technologies Used", size="5"),
#                 rx.text("• Frontend: Reflex"),
#                 rx.text("• Backend: Python"),
#                 rx.text("• LLM: Groq (LLaMA 3.1)"),
#                 rx.text("• Embeddings: Sentence Transformers"),
#                 rx.text("• Vector Database: ChromaDB"),
#                 rx.text("• Framework: LangChain"),

#                 rx.heading("🎯 Use Cases", size="5"),
#                 rx.text("• Academic research assistance"),
#                 rx.text("• Resume analysis"),
#                 rx.text("• Business document insights"),
#                 rx.text("• CSV data understanding"),
#                 rx.text("• Document summarization"),

#                 rx.heading("👩‍💻 Developer", size="5"),
#                 rx.text(
#                     "Developed as a Final Year Project focusing on AI-powered document "
#                     "understanding and intelligent retrieval systems."
#                 ),

#                 spacing="4",
#                 align="start",
#             ),
#             padding="30px",
#         ),

        
#     )

import reflex as rx
from DOCU_AI.components.navbar import navbar
from DOCU_AI.states.theme_state import ThemeState

def about():

    card_style = dict(
        padding="18px",
        border_radius="18px",
        backdrop_filter="blur(12px)",
        bg=rx.color_mode_cond(
            "rgba(255,255,255,0.65)",
            "rgba(30,41,59,0.55)"
        ),
        border="1px solid rgba(255,255,255,0.15)",
        box_shadow="0 8px 30px rgba(0,0,0,0.12)",
        transition="all 0.3s ease",
        _hover={
            "transform": "translateY(-6px) scale(1.02)",
            "box_shadow": "0 20px 60px rgba(0,0,0,0.25)",
        },
        width="100%",
    )

    return rx.box(
        navbar(),

        rx.container(
            rx.vstack(

                # 🔥 ANIMATED TITLE
                rx.heading(
                    "🧠 About DocuAI",
                    size="8",
                    background="linear-gradient(270deg, #4facfe, #00f2fe, #4facfe)",
                    background_size="400% 400%",
                    animation="gradientMove 6s ease infinite",
                    background_clip="text",
                    color="transparent",
                ),

                rx.text(
                    "AI-powered document intelligence for smart search & knowledge retrieval.",
                    font_size="16px",
                    text_align="center",
                    color=rx.color_mode_cond("#555", "#cbd5f5"),
                ),

                # 🔥 GRID SECTION
                rx.grid(

                    # COLUMN 1
                    rx.vstack(

                        rx.box(
                            rx.heading("⚙️ Features", size="4"),
                            rx.text("• Upload PDF, TXT"),
                            rx.text("• Natural language Q&A"),
                            rx.text("• Context-aware AI"),
                            rx.text("• Source tracking"),
                            rx.text("• Chat history"),
                            **card_style,
                        ),

                        rx.box(
                            rx.heading("🎯 Use Cases", size="4"),
                            rx.text("• Research assistance"),
                            rx.text("• Resume analysis"),
                            rx.text("• Business insights"),
                            rx.text("• CSV understanding"),
                            rx.text("• Summarization"),
                            **card_style,
                        ),

                        spacing="4",
                    ),

                    # COLUMN 2
                    rx.vstack(

                        rx.box(
                            rx.heading("🏗 Architecture", size="4"),
                            rx.text("1. Upload"),
                            rx.text("2. Processing"),
                            rx.text("3. Chunking"),
                            rx.text("4. Embeddings"),
                            rx.text("5. Vector DB"),
                            rx.text("6. Retrieval"),
                            rx.text("7. LLM Answer"),
                            **card_style,
                        ),

                        rx.box(
                            rx.heading("🧪 Tech Stack", size="4"),
                            rx.text("• Reflex (Frontend)"),
                            rx.text("• Python (Backend)"),
                            rx.text("• Groq LLaMA 3.1"),
                            rx.text("• Sentence Transformers"),
                            rx.text("• ChromaDB"),
                            rx.text("• LangChain"),
                            **card_style,
                        ),

                        spacing="4",
                    ),

                    columns="2",
                    spacing="6",
                    width="100%",
                ),

                # 🔥 INSANE QUOTE CARD
                rx.box(
                    rx.text(
                        "“AI will not replace humans, but humans with AI will replace those without it.”",
                        font_style="italic",
                        text_align="center",
                        font_size="17px",
                        color="white"
                    ),
                    rx.text(
                        "— Modern AI Philosophy",
                        text_align="center",
                        font_size="12px",
                        color="white"
                    ),

                    padding="22px",
                    border_radius="22px",
                    bg="linear-gradient(135deg, #4facfe, #00f2fe)",
                    box_shadow="0 15px 50px rgba(0,242,254,0.45)",
                    transition="all 0.3s ease",
                    _hover={
                        "transform": "scale(1.03)",
                        "box_shadow": "0 25px 80px rgba(0,242,254,0.6)",
                    },
                    width="100%",
                ),

                spacing="6",
                padding="30px",
                align="center",
            ),

            max_width="1100px",
        ),

        # 🔥 BACKGROUND GRADIENT
        # bg=rx.color_mode_cond(
        #     "linear-gradient(to right, #f8fbff, #eef6ff)",
        #     "linear-gradient(to right, #020617, #0f172a)"
        # ),
        bg=rx.cond(
            ThemeState.color_mode == "dark",
            "linear-gradient(to right, #020617, #0f172a)",
            "linear-gradient(to right, #f8fbff, #eef6ff)"
        ),

        min_height="100vh",
    )