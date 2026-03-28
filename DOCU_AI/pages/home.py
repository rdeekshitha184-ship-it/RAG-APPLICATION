# # import reflex as rx
# # from DOCU_AI.components.navbar import navbar
# # from DOCU_AI.components.hero import hero
# # from DOCU_AI.components.footer import footer

# # def home():
# #     return rx.vstack(
# #         navbar(),
# #         hero(),
# #         footer(),
# #     )

# import reflex as rx
# from DOCU_AI.components.navbar import navbar
# from DOCU_AI.components.hero import hero
# from DOCU_AI.components.footer import footer
# from DOCU_AI.pages.upload import UploadState


# def home():
#     return rx.vstack(

#         # NAVBAR
#         rx.box(
#             navbar(),
#             width="100%",
#             box_shadow="sm",
#         ),

#         # 🔥 HERO SECTION (LESS HEIGHT)
#         rx.box(
#             hero(),
#             width="100%",
#             max_width="1200px",
#             margin="auto",
#             padding="20px",   # 🔥 reduced
#         ),

#         # 🔥 CTA SECTION (COMPACT)
#         # rx.center(
#         #     rx.vstack(
#         #         rx.heading("Start Exploring Your Documents 🚀", size="5"),

#         #         rx.text(
#         #             "Upload documents and chat with them instantly using AI.",
#         #             color="gray",
#         #             text_align="center"
#         #         ),

#         #         rx.button(
#         #             " Go to Upload",
#         #             on_click=lambda: rx.redirect("/upload"),
#         #             size="2",   # 🔥 smaller button
#         #             color_scheme="blue",
#         #         ),

#         #         spacing="2",   # 🔥 tighter spacing
#         #         align="center",
#         #     ),
#         #     padding="20px",   # 🔥 reduced
#         # ),

#         # FOOTER
#         footer(),

#         spacing="2",   # 🔥 VERY IMPORTANT (was too large before)
#         bg=rx.cond(UploadState.dark_mode, "#0f172a", "#f8fafc"),
#         color=rx.cond(UploadState.dark_mode, "white", "black"),
#         min_height="100vh",
#         justify="between",   # 🔥 keeps footer at bottom nicely
#         width="100%",
#     )

#----------------------------------------------#
import reflex as rx
from DOCU_AI.components.navbar import navbar
from DOCU_AI.components.hero import hero
from DOCU_AI.components.footer import footer
from DOCU_AI.pages.upload import UploadState
from DOCU_AI.states.theme_state import ThemeState


def home():
    return rx.vstack(

        # NAVBAR
        rx.box(
            navbar(),
            width="100%",
            box_shadow="sm",
        ),

        # HERO ONLY
        rx.box(
            hero(),
            width="100%",
            max_width="1200px",
            margin="auto",
            padding="10px",   # 🔥 reduced further
        ),

        # FOOTER
        footer(),

        spacing="2",
        justify="between",   # 🔥 keeps footer at bottom
        bg=rx.cond(ThemeState.color_mode == "dark", "#0f172a", "#f8fafc"),
        color=rx.cond(ThemeState.color_mode == "dark", "white", "black"),
        min_height="100vh",
        width="100%",
    )
#---------------------------------------------#