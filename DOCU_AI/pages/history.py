
# import reflex as rx
# from DOCU_AI.components.navbar import navbar
# from DOCU_AI.components.footer import footer
# from DOCU_AI.states.rag_state import ChatState


# def history():

#     return rx.vstack(
#         navbar(),

#         rx.heading("📜 Chat History", size="8"),

#         # ✅ If no history
#         rx.cond(
#             ChatState.history == [],
#             rx.text("No chat history yet...", color="gray"),

#             # ✅ Loop through history
#             rx.foreach(
#                 ChatState.history,
#                 lambda item: rx.box(

#                     rx.text(f"🧑 Question: {item.question}", font_weight="bold"),
#                     rx.text(f"🤖 Answer: {item.answer}"),
#                     rx.text(f"📂 Sources: {item.sources}", font_size="sm", color="gray"),

#                     padding="15px",
#                     margin="10px 0",
#                     border="1px solid #ddd",
#                     border_radius="10px",
#                     width="100%",
#                 )
#             )
#         ),

#         # ✅ Clear Button
#         rx.button(
#             "🗑 Clear History",
#             color_scheme="red",
#             on_click=ChatState.clear_history,
#             margin_top="20px"
#         ),
#         rx.button(
#             "⬇ Download Chat History (PDF)",
#             color_scheme="green",
#             on_click=ChatState.download_chat,
#             margin_top="20px"
#         ),

#         #footer(),

#         padding="40px"
#     )
#---------------------------------------------#
#--------------------------------------------#
import reflex as rx

from DOCU_AI.components.navbar import navbar
from DOCU_AI.states.rag_state import ChatState
from DOCU_AI.states.theme_state import ThemeState

# 🔥 EXTENDED STATE
class HistoryState(ChatState):
    search_query: str = ""
    filter_doc: str = ""
    expanded_index: int = -1

    def set_search(self, value: str):
        self.search_query = value

    def set_filter(self, value: str):
        self.filter_doc = value

    def toggle_expand(self, index: int):
        if self.expanded_index == index:
            self.expanded_index = -1
        else:
            self.expanded_index = index


# 🔥 UI
def history():

    return rx.vstack(

        # NAVBAR
        rx.box(
            navbar(),
            width="100%",
            box_shadow="sm",
        ),

        # HEADER
        rx.heading("📜 Chat History", size="7"),

        # 🔍 SEARCH + FILTER
        rx.hstack(

            rx.input(
                placeholder="Search questions or answers...",
                value=HistoryState.search_query,
                on_change=HistoryState.set_search,
                width="60%",
            ),

            rx.input(
                placeholder="Filter by document name...",
                value=HistoryState.filter_doc,
                on_change=HistoryState.set_filter,
                width="40%",
            ),

            width="100%",
            max_width="900px",
            margin="auto",
        ),

        # MAIN CONTENT
        rx.box(

            rx.cond(
                HistoryState.history == [],
                rx.text("No chat history yet...", color="gray"),

                rx.vstack(
                    rx.foreach(
                        HistoryState.history,
                        lambda item, index: rx.cond(

                            # 🔥 FILTER LOGIC
                            (
                                (HistoryState.search_query == "")
                                | (item.question.contains(HistoryState.search_query))
                                | (item.answer.contains(HistoryState.search_query))
                            )
                            &
                            (
                                (HistoryState.filter_doc == "")
                                | (item.sources.contains(HistoryState.filter_doc))
                            ),

                            # 🔥 CARD
                            rx.box(
                                rx.vstack(

                                    # QUESTION
                                    rx.text(
                                        f"🧑 {item.question}",
                                        font_weight="bold",
                                        font_size="16px"
                                    ),

                                    # 🔥 EXPAND BUTTON + ANSWER
                                    rx.vstack(

                                        rx.button(
                                            rx.cond(
                                                HistoryState.expanded_index == index,
                                                "Hide Answer",
                                                "View Answer"
                                            ),
                                            size="1",
                                            variant="outline",
                                            on_click=HistoryState.toggle_expand(index)
                                        ),

                                        rx.cond(
                                            HistoryState.expanded_index == index,
                                            rx.text(item.answer, white_space="pre-wrap"),
                                            rx.fragment()
                                        )
                                    ),

                                    # SOURCES
                                    rx.text(
                                        f"📄 {item.sources}",
                                        font_size="12px",
                                        color="gray"
                                    ),

                                ),

                                padding="15px",
                                border_radius="12px",
                                bg=rx.cond(ThemeState.color_mode == "dark", "#1e293b", "white"),
                                color=rx.cond(ThemeState.color_mode == "dark", "white", "black"),
                                box_shadow="sm",
                                width="100%",
                            ),

                            # if not match → render nothing
                            rx.fragment()
                        )
                    ),
                    spacing="4",
                    width="100%",
                )
            ),

            width="100%",
            max_width="900px",
            margin="auto",
        ),

        # BUTTONS
        rx.hstack(
            rx.button(
                "🗑 Clear History",
                color_scheme="red",
                on_click=HistoryState.clear_history,
                variant="outline"
            ),

            rx.button(
                "⬇ Download PDF",
                color_scheme="green",
                on_click=HistoryState.download_chat,
            ),

            spacing="4",
            justify="center",
            width="100%",
            max_width="900px",
            margin="auto",
        ),

        spacing="6",
        padding="30px",
        bg=rx.cond(ThemeState.color_mode == "dark", "#0f172a", "#f1f5f9"),
        color=rx.cond(ThemeState.color_mode == "dark", "white", "black"),
        min_height="100vh",
        width="100%",
    )