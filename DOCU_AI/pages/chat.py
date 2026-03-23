
import reflex as rx

from DOCU_AI.components.navbar import navbar
from DOCU_AI.components.footer import footer
from DOCU_AI.states.rag_state import ChatState


def chat() -> rx.Component:
    return rx.vstack(
        navbar(),

        # Heading
        rx.heading("Chat with your Documents", size="5"),

        # Chat history display (UPDATED)
        rx.box(
            rx.foreach(
                ChatState.history,
                lambda item: rx.vstack(
                    
                    # ✅ USER MESSAGE (RIGHT SIDE)
                    rx.hstack(
                        rx.spacer(),
                        rx.box(
                            rx.text(item.question),
                            bg="#1e90ff",
                            color="white",
                            padding="10px",
                            border_radius="12px",
                            max_width="60%",
                        ),
                        width="100%",
                    ),

                    # ✅ AI MESSAGE (LEFT SIDE)
                    rx.hstack(
                        rx.box(
                            rx.text(item.answer, white_space="pre-wrap"),
                            bg="#f1f1f1",
                            padding="10px",
                            border_radius="12px",
                            max_width="60%",
                        ),
                        rx.spacer(),
                        width="100%",
                    ),

                    # ✅ SOURCES
                    rx.hstack(
                        rx.text(
                            "Sources: " + item.sources,
                            font_size="10px",
                            color="gray"
                        ),
                        rx.spacer(),
                        width="100%",
                    ),

                    spacing="2",
                    width="100%",
                ),
            ),
            width="100%",
        ),

        # ✅ LOADING SPINNER (NEW)
        rx.cond(
            ChatState.is_loading,
            rx.hstack(
                rx.spinner(),
                rx.text("Thinking..."),
                justify="center",
                width="100%",
            )
        ),

        # Input + Button (same as yours)
        rx.hstack(
            rx.input(
                placeholder="Ask something...",
                value=ChatState.question,
                on_change=ChatState.set_question,
                width="80%",
            ),
            rx.button(
                "Ask",
                on_click=ChatState.ask_question,
                color_scheme="blue",
            ),
            width="100%",
        ),

        spacing="4",
        padding="20px",
        width="100%",
    )