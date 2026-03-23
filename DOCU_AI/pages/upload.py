
# import reflex as rx
# import os
# components.navbar import navbar.components.footer import footer.backend.rag import build_vectorstore

# # Ensure folder exists
# # UPLOAD_DIR = "documents"
# # os.makedirs(UPLOAD_DIR, exist_ok=True)

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# UPLOAD_DIR = os.path.join(BASE_DIR, "documents")

# os.makedirs(UPLOAD_DIR, exist_ok=True)


# class UploadState(rx.State):

#     async def handle_upload(self, files: list[rx.UploadFile]):
#         for file in files:
#             save_path = os.path.join(UPLOAD_DIR, file.filename)

#             content = await file.read()

#             with open(save_path, "wb") as f:
#                 f.write(content)
              


# def upload():
#     return rx.vstack(
#         navbar(),

#         rx.heading("Upload Documents"),

#         # Upload button
#         rx.upload(
#             rx.button("Upload File"),
#             id="upload1",
#         ),

#         rx.button(
#             "Submit",
#             on_click=UploadState.handle_upload(
#                 rx.upload_files(upload_id="upload1")
#             )
#         ),

#         rx.heading("Uploaded Files"),

#         # ✅ Always read from folder (no disappearing)
#         rx.foreach(
#             os.listdir(UPLOAD_DIR),
#             lambda file: rx.text(f"📄 {file}")
#         ),

#         #footer(),
#         spacing="4",
#         )



import reflex as rx
import os

from DOCU_AI.components.navbar import navbar
from DOCU_AI.components.footer import footer
from DOCU_AI.backend.rag import build_vectorstore

# Ensure folder exists
# UPLOAD_DIR = "documents"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, "documents")

os.makedirs(UPLOAD_DIR, exist_ok=True)


class UploadState(rx.State):

    async def handle_upload(self, files: list[rx.UploadFile]):
        for file in files:
            save_path = os.path.join(UPLOAD_DIR, file.filename)

            content = await file.read()

            with open(save_path, "wb") as f:
                f.write(content)
              


def upload():
    return rx.vstack(
        navbar(),

        rx.heading("Upload Documents"),

        # Upload button
        rx.upload(
            rx.button("Upload File"),
            id="upload1",
        ),

        rx.button(
            "Submit",
            on_click=UploadState.handle_upload(
                rx.upload_files(upload_id="upload1")
            )
        ),

        rx.heading("Uploaded Files"),

        # ✅ Always read from folder (no disappearing)
        rx.foreach(
            os.listdir(UPLOAD_DIR),
            lambda file: rx.text(f"📄 {file}")
        ),

        #footer(),
        spacing="4",
        padding="20px"
    )