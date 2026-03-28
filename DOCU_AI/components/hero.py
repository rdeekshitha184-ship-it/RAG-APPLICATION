# # # import reflex as rx

# # # def hero():
# # #     return rx.hstack(
# # #             # LEFT SIDE TEXT
# # #             rx.vstack(
# # #                 rx.text("DocuSearch AI", color="gray", font_size="18px"),

# # #                 rx.heading(
# # #                     "AI Based Document\nSearch & Knowledge Retrieval",
# # #                     size="9",
# # #                     weight="bold"
# # #                 ),

# # #                 rx.text(
# # #                     "Chat with your documents using advanced AI",
# # #                     color="gray"
# # #                 ),

# # #                 rx.button(
# # #                     "Get Started",
# # #                     #quote(),
# # #                     color_scheme="blue",
# # #                     size="3",
# # #                     margin_top="10px"
# # #                 ),

# # #                 align="start",
# # #                 spacing="4",
# # #                 width="50%",
# # #             ),

# # #             # RIGHT SIDE IMAGE
# # #             rx.image(
# # #                 src="/logo.jpeg",  # put image in assets folder
# # #                 width="300px"
# # #             ),
            
# # #             justify="between",
# # #             align="center",
# # #             padding="60px",
# # #         )

# # # # def quote():
# # # #     return rx.box(
# # # #         rx.text("Qoute..."),
# # # #         rx.text("Author...")
# # # #     )

# # import reflex as rx
# # from DOCU_AI.pages.upload import UploadState


# # def hero():
# #     return rx.hstack(

# #         # LEFT SIDE
# #         rx.vstack(
# #             rx.text(
# #                 "DocuSearch AI",
# #                 color="gray",
# #                 font_size="16px"
# #             ),

# #             rx.heading(
# #                 "AI Based Document\nSearch & Knowledge Retrieval",
# #                 size="8",   # 🔥 slightly reduced
# #                 weight="bold"
# #             ),

# #             rx.text(
# #                 "Chat with your documents using advanced AI",
# #                 color="gray"
# #             ),

# #             rx.button(
# #                 "Get Started",
# #                 on_click=lambda: rx.redirect("/upload"),  # 🔥 better UX
# #                 color_scheme="blue",
# #                 size="2",
# #                 margin_top="10px"
# #             ),

# #             align="start",
# #             spacing="3",   # 🔥 tighter
# #             width="50%",
# #         ),

# #         # RIGHT SIDE IMAGE
# #         rx.image(
# #             src="/logo.jpeg",
# #             width="260px",   # 🔥 slightly smaller
# #             border_radius="12px"
# #         ),

# #         justify="between",
# #         align="center",

# #         # 🔥 FIXED SPACING
# #         padding="30px",   # ❗ reduced from 60 → 30
# #         min_height="60vh",  # 🔥 controlled height

# #         width="100%",
# #     )

import reflex as rx
from DOCU_AI.states.theme_state import ThemeState


def hero():
    return rx.hstack(

        # LEFT SIDE
        rx.vstack(
            rx.text(
                "DocuSearch AI",
                color="gray",
                font_size="16px"
            ),

            rx.heading(
                "AI Based Document\nSearch & Knowledge Retrieval",
                size="9",   # 🔥 back to bigger size
                weight="bold"
            ),

            rx.text(
                "Chat with your documents using advanced AI",
                color="gray"
            ),

            rx.button(
                "-> Get Started",
                on_click=lambda: rx.redirect("/upload"),
                color_scheme="blue",
                size="3",
                margin_top="10px"
            ),

            align="start",
            spacing="4",
            width="50%",
        ),

        # RIGHT SIDE IMAGE (🔥 FIXED)
        rx.box(
            rx.image(
                src="/logo.jpeg",
                width="300px",
            ),

            # 🔥 MAGIC FIX FOR WHITE BG IMAGE
            bg=rx.cond(
                ThemeState.color_mode == "dark",
                "#1e293b",   # dark card background
                "#f1f5f9"    # light soft background
            ),

            padding="15px",
            border_radius="16px",
            box_shadow="lg",
        ),

        justify="between",
        align="center",

        # 🔥 FIXED HEIGHT
        min_height="75vh",   # 🔥 increased from 60 → 75
        padding="40px",

        width="100%",
    )


# import reflex as rx

# from DOCU_AI.pages.upload import UploadState

# from DOCU_AI.pages.upload import UploadState


# def hero():
#     return rx.hstack(

#         # LEFT SIDE
#         rx.vstack(
#             rx.text(
#                 "DocuSearch AI",
#                 color="gray",
#                 font_size="16px"
#             ),

#             rx.heading(
#                 "AI Based Document\nSearch & Knowledge Retrieval",
#                 size="9",
#                 weight="bold"
#             ),

#             rx.text(
#                 "Chat with your documents using advanced AI",
#                 color="gray"
#             ),

#             rx.button(
#                 "➡️ Get Started",
#                 on_click=lambda: rx.redirect("/upload"),
#                 size="3",
#                 margin_top="10px",

#                 background="linear-gradient(to right, #3b82f6, #06b6d4)",
#                 color="white",

#                 border_radius="10px",
#                 padding="10px 20px",
#                 box_shadow="md",

#                 _hover={
#                     "opacity": "0.9",
#                     "transform": "scale(1.05)"
#                 }
#             ),

#             align="start",
#             spacing="4",
#             width="50%",
#         ),

#         # RIGHT SIDE IMAGE (NO BACKEND DEPENDENCY)
#         rx.box(
#             rx.image(
#                 src="/logo.jpeg",
#                 width="300px",
#             ),

#             bg="#f1f5f9",  # ✅ safe
#             padding="15px",
#             border_radius="16px",
#             box_shadow="lg",
#             # bg=rx.cond(
#             #     UploadState.dark_mode,
#             #     "#1e293b",   # dark card background
#             #     "#f1f5f9"    # light soft background
#             # ),
#         ),

#         justify="between",
#         align="center",

#         min_height="75vh",
#         padding="40px",

#         width="100%",
#     )