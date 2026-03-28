
# import reflex as rx

# from DOCU_AI.components.navbar import navbar
# from DOCU_AI.components.footer import footer
# from DOCU_AI.states.rag_state import ChatState


# def chat() -> rx.Component:
#     return rx.vstack(
#         navbar(),

#         # Heading
#         rx.heading("Chat with your Documents", size="5"),

#         # Chat history display (UPDATED)
#         rx.box(
#             rx.foreach(
#                 ChatState.history,
#                 lambda item: rx.vstack(
                    
#                     # ✅ USER MESSAGE (RIGHT SIDE)
#                     rx.hstack(
#                         rx.spacer(),
#                         rx.box(
#                             rx.text(item.question),
#                             bg="#1e90ff",
#                             color="white",
#                             padding="10px",
#                             border_radius="12px",
#                             max_width="60%",
#                         ),
#                         width="100%",
#                     ),

#                     # ✅ AI MESSAGE (LEFT SIDE)
#                     rx.hstack(
#                         rx.box(
#                             rx.text(item.answer, white_space="pre-wrap"),
#                             bg="#f1f1f1",
#                             padding="10px",
#                             border_radius="12px",
#                             max_width="60%",
#                         ),
#                         rx.spacer(),
#                         width="100%",
#                     ),

#                     # ✅ SOURCES
#                     rx.hstack(
#                         rx.text(
#                             "Sources: " + item.sources,
#                             font_size="10px",
#                             color="gray"
#                         ),
#                         rx.spacer(),
#                         width="100%",
#                     ),

#                     spacing="2",
#                     width="100%",
#                 ),
#             ),
#             width="100%",
#         ),

#         # ✅ LOADING SPINNER (NEW)
#         rx.cond(
#             ChatState.is_loading,
#             rx.hstack(
#                 rx.spinner(),
#                 rx.text("Thinking..."),
#                 justify="center",
#                 width="100%",
#             )
#         ),

#         # Input + Button (same as yours)
#         rx.hstack(
#             rx.input(
#                 placeholder="Ask something...",
#                 value=ChatState.question,
#                 on_change=ChatState.set_question,
#                 width="80%",
#             ),
#             rx.button(
#                 "Ask",
#                 on_click=ChatState.ask_question,
#                 color_scheme="blue",
#             ),
#             width="100%",
#         ),

#         spacing="4",
#         padding="20px",
#         width="100%",
#     )

import reflex as rx

from DOCU_AI.components.navbar import navbar
from DOCU_AI.states.rag_state import ChatState
from DOCU_AI.states.theme_state import ThemeState


def chat() -> rx.Component:
    return rx.vstack(

        # NAVBAR
        rx.box(
            navbar(),
            width="100%",
            box_shadow="sm",
        ),

        # HEADER
        rx.hstack(
            rx.heading("💬 Chat with your Documents", size="6"),
            rx.spacer(),
            rx.button(
                "Clear",
                on_click=ChatState.clear_history,
                variant="outline",
                color_scheme="red"
            ),
            width="100%",
            max_width="900px",
            margin="auto",
        ),

        # CHAT CONTAINER
        rx.box(

            # Empty state
            rx.cond(
                ChatState.history == [],
                rx.text("Start asking questions 👇", color="gray"),
            ),

            rx.foreach(
                ChatState.history,
                lambda item: rx.vstack(

                    # USER MESSAGE
                    rx.hstack(
                        rx.spacer(),
                        rx.box(
                            rx.text(item.question),
                            bg="#2563eb",
                            color="white",
                            padding="12px",
                            border_radius="16px",
                            max_width="70%",
                        ),
                        width="100%",
                    ),

                    # AI MESSAGE
                    rx.hstack(
                        rx.box(
                            rx.vstack(

                                # 🔥 Typing effect simulation
                                rx.cond(
                                    ChatState.is_loading,
                                    rx.text("Typing...", color="gray"),
                                    rx.text(item.answer, white_space="pre-wrap"),
                                ),

                                rx.text(
                                    f"📄 {item.sources}",
                                    font_size="12px",
                                    color="gray",
                                ),
                            ),
                            bg=rx.cond(ThemeState.color_mode == "dark", "#1e293b", "#f1f5f9"),
                            color=rx.cond(ThemeState.color_mode == "dark", "white", "black"),
                            padding="12px",
                            border_radius="16px",
                            max_width="70%",
                        ),
                        rx.spacer(),
                        width="100%",
                    ),

                    spacing="3",
                    width="100%",
                ),
            ),

            # 🔥 AUTO SCROLL (hack using anchor)
            rx.box(id="chat-bottom"),

            height="500px",
            overflow_y="auto",
            padding="15px",
            border_radius="12px",
            border="1px solid #e5e7eb",
            bg=rx.cond(ThemeState.color_mode == "dark", "#0f172a", "white"),
            width="100%",
            max_width="900px",
            margin="auto",
        ),

        # LOADING
        rx.cond(
            ChatState.is_loading,
            rx.hstack(
                rx.spinner(),
                rx.text("Thinking..."),
                justify="center",
                width="100%",
            )
        ),

        # INPUT BAR
        rx.hstack(
            rx.input(
                placeholder="Ask something about your documents...",
                value=ChatState.question,
                on_change=ChatState.set_question,

                # 🔥 ENTER KEY SUPPORT
                on_key_down=lambda key: rx.cond(
                    key == "Enter",
                    ChatState.ask_question(),
                    rx.noop()
                ),

                width="100%",
                size="3",
            ),
            rx.button(
                "Ask",
                on_click=ChatState.ask_question,
                color_scheme="blue",
                size="3",
            ),
            width="100%",
            max_width="900px",
            margin="auto",
        ),

        spacing="5",
        padding="30px",
        bg=rx.cond(ThemeState.color_mode == "dark", "#0f172a", "#f1f5f9"),
        color=rx.cond(ThemeState.color_mode == "dark", "white", "black"),
        min_height="100vh",
        width="100%",
    )