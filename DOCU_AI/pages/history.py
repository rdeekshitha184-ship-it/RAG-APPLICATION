
import reflex as rx
from DOCU_AI.components.navbar import navbar
from DOCU_AI.components.footer import footer
from DOCU_AI.states.rag_state import ChatState


def history():

    return rx.vstack(
        navbar(),

        rx.heading("📜 Chat History", size="8"),

        # ✅ If no history
        rx.cond(
            ChatState.history == [],
            rx.text("No chat history yet...", color="gray"),

            # ✅ Loop through history
            rx.foreach(
                ChatState.history,
                lambda item: rx.box(

                    rx.text(f"🧑 Question: {item.question}", font_weight="bold"),
                    rx.text(f"🤖 Answer: {item.answer}"),
                    rx.text(f"📂 Sources: {item.sources}", font_size="sm", color="gray"),

                    padding="15px",
                    margin="10px 0",
                    border="1px solid #ddd",
                    border_radius="10px",
                    width="100%",
                )
            )
        ),

        # ✅ Clear Button
        rx.button(
            "🗑 Clear History",
            color_scheme="red",
            on_click=ChatState.clear_history,
            margin_top="20px"
        ),
        rx.button(
            "⬇ Download Chat History (PDF)",
            color_scheme="green",
            on_click=ChatState.download_chat,
            margin_top="20px"
        ),

        #footer(),

        padding="40px"
    )
