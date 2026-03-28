
# # import reflex as rx

# # def navbar():
# #     return rx.box(
# #         rx.hstack(
# #             rx.text("DocuAI", font_size="24px", font_weight="bold", color="white"),

# #             rx.spacer(),

# #             rx.hstack(
# #                 rx.link("Home", href="/"),
# #                 rx.link("UploadDocument", href="/upload"),
# #                 rx.link("Chat", href="/chat"),
# #                 rx.link("ChatHistory", href="/history"),
# #                 rx.link("About", href="/about"),
# #                 spacing="5",
# #                 color="white"
# #             ),
# #             width="100%",
# #             padding="15px"
# #         ),
# #         width="100%",
# #         bg="linear-gradient(to right, #4facfe, #00f2fe)",
# #         margin="0",
# #         padding="0"
# #     )


# #---------------------------------------------#
# import reflex as rx

# def navbar():
#     return rx.box(
#         rx.hstack(

#             # 🔥 LOGO
#             rx.text(
#                 "DocuAI",
#                 font_size="26px",
#                 font_weight="bold",
#                 color="white"
#             ),

#             rx.spacer(),

#             # 🔥 NAV LINKS
#             rx.hstack(

#                 rx.link(
#                     "Home",
#                     href="/",
#                     font_size="16px",
#                     font_weight="bold",
#                     color="white",
#                     _hover={"color": "#e0f7ff"}
#                 ),

#                 rx.link(
#                     "Upload",
#                     href="/upload",
#                     font_size="16px",
#                     font_weight="bold",
#                     color="white",
#                     _hover={"color": "#e0f7ff"}
#                 ),

#                 rx.link(
#                     "Chat",
#                     href="/chat",
#                     font_size="16px",
#                     font_weight="bold",
#                     color="white",
#                     _hover={"color": "#e0f7ff"}
#                 ),

#                 rx.link(
#                     "History",
#                     href="/history",
#                     font_size="16px",
#                     font_weight="bold",
#                     color="white",
#                     _hover={"color": "#e0f7ff"}
#                 ),

#                 rx.link(
#                     "About",
#                     href="/about",
#                     font_size="16px",
#                     font_weight="bold",
#                     color="white",
#                     _hover={"color": "#e0f7ff"}
#                 ),

#                 spacing="6",
#             ),

#             width="100%",
#             padding="15px 30px",  # 🔥 better spacing
#             align="center"
#         ),

#         width="100%",

#         # 🔥 SAME GRADIENT BUT BETTER LOOK
#         bg="linear-gradient(to right, #3b82f6, #06b6d4)",

#         box_shadow="md",   # 🔥 adds depth
#     )   
# #---------------------------------------------#


import reflex as rx
from DOCU_AI.states.theme_state import ThemeState

def navbar():
    return rx.box(
        rx.hstack(

            rx.text("DocuAI", font_size="26px", font_weight="bold", color="white"),

            rx.spacer(),

            rx.hstack(
                rx.link("Home", href="/", color="white"),
                rx.link("Upload", href="/upload", color="white"),
                rx.link("Chat", href="/chat", color="white"),
                rx.link("History", href="/history", color="white"),
                rx.link("About", href="/about", color="white"),
                spacing="6",
                font_weight="bold"
            ),

            rx.spacer(),

            # 🌙 GLOBAL TOGGLE
            rx.button(
                rx.cond(
                    ThemeState.color_mode == "dark",
                    "☀️",
                    "🌙"
                ),
                on_click=ThemeState.toggle_theme,
                variant="outline",
                color="white"
            ),

            padding="15px 30px",
            width="100%"
        ),
        bg="linear-gradient(to right, #3b82f6, #06b6d4)",
    )