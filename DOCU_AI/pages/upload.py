
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


#--------------------------------------------------------------
# import reflex as rx
# import os

# from DOCU_AI.components.navbar import navbar
# from DOCU_AI.components.footer import footer
# from DOCU_AI.backend.rag import build_vectorstore

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
#         padding="20px"
#     )

#-----------------------------------------

# import reflex as rx
# import os

# from DOCU_AI.components.navbar import navbar
# from DOCU_AI.backend.rag import build_vectorstore

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# UPLOAD_DIR = os.path.join(BASE_DIR, "documents")

# os.makedirs(UPLOAD_DIR, exist_ok=True)


# # 🔥 STATE
# class UploadState(rx.State):
#     is_uploading: bool = False
#     status_message: str = ""
#     show_popup: bool = False
#     dark_mode: bool = False

#     def toggle_theme(self):
#         self.dark_mode = not self.dark_mode

#     async def start_upload(self, files: list[rx.UploadFile]):
#         self.is_uploading = True
#         self.status_message = "Uploading files..."
#         yield

#         for file in files:
#             save_path = os.path.join(UPLOAD_DIR, file.filename)
#             content = await file.read()

#             with open(save_path, "wb") as f:
#                 f.write(content)

#         self.status_message = "Processing documents..."
#         yield

#         build_vectorstore()

#         self.status_message ="✅ Upload complete!"
#         yield

#         self.is_uploading = False
#         yield

#         self.show_popup = True
#         yield

#     def delete_file(self, filename: str):
#         file_path = os.path.join(UPLOAD_DIR, filename)

#         if os.path.exists(file_path):
#             os.remove(file_path)

#         build_vectorstore()

#     def go_to_chat(self):
#         self.show_popup = False
#         return rx.redirect("/chat")

#     def stay_here(self):
#         self.show_popup = False


# # 🔥 UI
# def upload():
#     return rx.vstack(

#         # NAVBAR
#         rx.box(
#             navbar(),
#             width="100%",
#             box_shadow="sm",
#         ),

#         # 🌙 DARK MODE BUTTON
#         rx.hstack(
#             rx.spacer(),
#             rx.button(
#                 rx.cond(UploadState.dark_mode, "🌞 Light", "🌙 Dark"),
#                 on_click=UploadState.toggle_theme,
#                 variant="outline",
#             ),
#             width="100%",
#         ),

#         # MAIN CONTENT
#         rx.hstack(

#             # LEFT SIDE (UPLOAD)
#             rx.box(
#                 rx.vstack(
#                     rx.heading("📂 Upload Documents", size="6"),

#                     rx.text(
#                         "Upload PDF or TXT files and start chatting instantly.",
#                         color="gray"
#                     ),

#                     rx.box(
#                         rx.vstack(

#                             # UPLOAD AREA
#                             rx.upload(
#                                 rx.vstack(
#                                     rx.text("📁 Drag & Drop files", font_size="18px", font_weight="bold"),
#                                     rx.text("or click to browse", color="gray"),
#                                 ),
#                                 id="upload1",
#                                 border="2px dashed #94a3b8",
#                                 padding="50px",
#                                 border_radius="16px",
#                                 width="100%",
#                                 bg=rx.cond(UploadState.dark_mode, "#0f172a", "#f8fafc"),
#                             ),

#                             # STATUS
#                             rx.cond(
#                                 UploadState.is_uploading,
#                                 rx.box(
#                                     rx.hstack(
#                                         rx.spinner(),
#                                         rx.text(UploadState.status_message),
#                                     ),
#                                     padding="10px",
#                                     border_radius="8px",
#                                     bg=rx.cond(UploadState.dark_mode, "#1e293b", "#e0f2fe"),
#                                     width="100%",
#                                 )
#                             ),

#                             # BUTTON
#                             rx.button(
#                                 "🚀 Upload Files",
#                                 on_click=lambda: UploadState.start_upload(
#                                     rx.upload_files(upload_id="upload1")
#                                 ),
#                                 color_scheme="blue",
#                                 width="100%",
#                             ),

#                         ),
#                         padding="25px",
#                         border_radius="16px",
#                         bg=rx.cond(UploadState.dark_mode, "#1e293b", "white"),
#                         color=rx.cond(UploadState.dark_mode, "white", "black"),
#                         box_shadow="lg",
#                         width="100%",
#                     ),

#                 ),
#                 width="45%",
#             ),

#             # RIGHT SIDE (FILES)
#             rx.box(
#                 rx.vstack(
#                     rx.heading("📄 Uploaded Files", size="6"),

#                     rx.cond(
#                         len(os.listdir(UPLOAD_DIR)) == 0,

#                         rx.text("No files uploaded yet 📭", color="gray"),

#                         rx.vstack(
#                             rx.foreach(
#                                 os.listdir(UPLOAD_DIR),
#                                 lambda file: rx.box(
#                                     rx.hstack(
#                                         rx.text(
#                                             f"📄 {file}",
#                                             font_weight="medium",
#                                         ),

#                                         rx.spacer(),

#                                         rx.text("Ready", color="green", font_size="12px"),

#                                         rx.button(
#                                             "Delete",
#                                             color_scheme="red",
#                                             size="1",
#                                             variant="soft",
#                                             on_click=UploadState.delete_file(file)
#                                         ),
#                                     ),
#                                     padding="12px",
#                                     border_radius="10px",
#                                     bg=rx.cond(UploadState.dark_mode, "#1e293b", "white"),
#                                     color=rx.cond(UploadState.dark_mode, "white", "black"),
#                                     box_shadow="sm",
#                                     width="100%",
#                                 ),
#                             ),
#                             spacing="3",
#                             width="100%",
#                         ),
#                     ),

#                 ),
#                 width="55%",
#             ),

#             spacing="8",
#             width="100%",
#         ),

#         # POPUP
#         rx.cond(
#             UploadState.show_popup,
#             rx.box(
#                 rx.center(
#                     rx.box(
#                         rx.vstack(
#                             rx.heading("✅ Upload Complete!", size="5"),
#                             rx.text("What would you like to do next?"),

#                             rx.hstack(
#                                 rx.button(
#                                     "Upload More",
#                                     on_click=UploadState.stay_here,
#                                     variant="outline"
#                                 ),
#                                 rx.button(
#                                     "Go to Chat",
#                                     on_click=UploadState.go_to_chat,
#                                     color_scheme="blue"
#                                 ),
#                             ),

#                             spacing="4",
#                             align="center"
#                         ),
#                         bg=rx.cond(UploadState.dark_mode, "#1e293b", "white"),
#                         color=rx.cond(UploadState.dark_mode, "white", "black"),
#                         padding="30px",
#                         border_radius="12px",
#                         box_shadow="xl",
#                     ),
#                 ),
#                 position="fixed",
#                 top="0",
#                 left="0",
#                 width="100%",
#                 height="100%",
#                 bg="rgba(0,0,0,0.5)",
#                 z_index="999",
#             )
#         ),

#         padding="40px",
#         bg=rx.cond(UploadState.dark_mode, "#0f172a", "#f1f5f9"),
#         color=rx.cond(UploadState.dark_mode, "white", "black"),
#         min_height="100vh",
#         width="100%",
#     )

# #----------------------------------------------#
# import reflex as rx
# import os

# from DOCU_AI.components.navbar import navbar
# from DOCU_AI.backend.rag import build_vectorstore
# from DOCU_AI.states.theme_state import ThemeState

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# UPLOAD_DIR = os.path.join(BASE_DIR, "documents")

# os.makedirs(UPLOAD_DIR, exist_ok=True)


# # 🔥 STATE
# class UploadState(rx.State):
#     is_uploading: bool = False
#     status_message: str = ""
#     dark_mode: bool = False

#     def toggle_theme(self):
#         self.dark_mode = not self.dark_mode

#     async def start_upload(self, files: list[rx.UploadFile]):
#         self.is_uploading = True
#         self.status_message = "Uploading files..."
#         yield

#         for file in files:
#             save_path = os.path.join(UPLOAD_DIR, file.filename)
#             content = await file.read()

#             with open(save_path, "wb") as f:
#                 f.write(content)

#         self.status_message = "Processing documents..."
#         yield

#         build_vectorstore()

#         self.status_message = "✅ Upload complete!"
#         yield

#         self.is_uploading = False
#         yield

#     def delete_file(self, filename: str):
#         file_path = os.path.join(UPLOAD_DIR, filename)

#         if os.path.exists(file_path):
#             os.remove(file_path)

#         build_vectorstore()


# # 🔥 UI
# def upload():
#     return rx.vstack(

#         # NAVBAR
#         rx.box(
#             navbar(),
#             width="100%",
#             box_shadow="sm",
#         ),

#         # 🌙 DARK MODE BUTTON
#         rx.hstack(
#             rx.spacer(),
#             rx.button(
#                 rx.cond(UploadState.dark_mode, "🌞 Light", "🌙 Dark"),
#                 on_click=UploadState.toggle_theme,
#                 variant="outline",
#             ),
#             width="100%",
#         ),

#         # MAIN CONTENT
#         rx.hstack(

#             # LEFT SIDE (UPLOAD)
#             rx.box(
#                 rx.vstack(
#                     rx.heading("📂 Upload Documents", size="6"),

#                     rx.text(
#                         "Upload PDF or TXT files and start chatting instantly.",
#                         color="gray"
#                     ),

#                     rx.box(
#                         rx.vstack(

#                             # UPLOAD AREA
#                             rx.upload(
#                                 rx.vstack(
#                                     rx.text("📁 Drag & Drop files", font_size="18px", font_weight="bold"),
#                                     rx.text("or click to browse", color="gray"),
#                                 ),
#                                 id="upload1",
#                                 border="2px dashed #94a3b8",
#                                 padding="50px",
#                                 border_radius="16px",
#                                 width="100%",
#                                 bg=rx.cond(UploadState.dark_mode, "#0f172a", "#f8fafc"),
#                             ),

#                             # STATUS
#                             rx.cond(
#                                 UploadState.is_uploading,
#                                 rx.box(
#                                     rx.hstack(
#                                         rx.spinner(),
#                                         rx.text(UploadState.status_message),
#                                     ),
#                                     padding="10px",
#                                     border_radius="8px",
#                                     bg=rx.cond(UploadState.dark_mode, "#1e293b", "#e0f2fe"),
#                                     width="100%",
#                                 )
#                             ),

#                             # SUCCESS MESSAGE (instead of popup)
#                             rx.cond(
#                                 UploadState.status_message == "✅ Upload complete!",
#                                 rx.text(
#                                     "Files uploaded successfully 🎉",
#                                     color="green",
#                                     font_size="14px",
#                                 )
#                             ),

#                             # BUTTON
#                             rx.button(
#                                 "🚀 Upload Files",
#                                 on_click=lambda: UploadState.start_upload(
#                                     rx.upload_files(upload_id="upload1")
#                                 ),
#                                 color_scheme="blue",
#                                 width="100%",
#                             ),

#                         ),
#                         padding="25px",
#                         border_radius="16px",
#                         bg=rx.cond(UploadState.dark_mode, "#1e293b", "white"),
#                         color=rx.cond(UploadState.dark_mode, "white", "black"),
#                         box_shadow="lg",
#                         width="100%",
#                     ),

#                 ),
#                 width="45%",
#             ),

#             # RIGHT SIDE (FILES)
#             rx.box(
#                 rx.vstack(
#                     rx.heading("📄 Uploaded Files", size="6"),

#                     rx.cond(
#                         len(os.listdir(UPLOAD_DIR)) == 0,
#                         rx.text("No files uploaded yet 📭", color="gray"),

#                         rx.vstack(
#                             rx.foreach(
#                                 os.listdir(UPLOAD_DIR),
#                                 lambda file: rx.box(
#                                     rx.hstack(
#                                         rx.text(f"📄 {file}", font_weight="medium"),

#                                         rx.spacer(),

#                                         rx.text("Ready", color="green", font_size="12px"),

#                                         rx.button(
#                                             "Delete",
#                                             color_scheme="red",
#                                             size="1",
#                                             variant="soft",
#                                             on_click=UploadState.delete_file(file)
#                                         ),
#                                     ),
#                                     padding="12px",
#                                     border_radius="10px",
#                                     bg=rx.cond(UploadState.dark_mode, "#1e293b", "white"),
#                                     color=rx.cond(UploadState.dark_mode, "white", "black"),
#                                     box_shadow="sm",
#                                     width="100%",
#                                 ),
#                             ),
#                             spacing="3",
#                             width="100%",
#                         ),
#                     ),

#                 ),
#                 width="55%",
#             ),

#             spacing="8",
#             width="100%",
#         ),

#         padding="40px",
#         bg=rx.cond(UploadState.dark_mode, "#0f172a", "#f1f5f9"),
#         color=rx.cond(UploadState.dark_mode, "white", "black"),
#         min_height="100vh",
#         width="100%",
#     )
# #-----------------------------------------------#
import reflex as rx
import os

from DOCU_AI.components.navbar import navbar
from DOCU_AI.backend.rag import build_vectorstore
from DOCU_AI.states.theme_state import ThemeState

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, "documents")

os.makedirs(UPLOAD_DIR, exist_ok=True)


# 🔥 STATE (CLEAN)
class UploadState(rx.State):
    is_uploading: bool = False
    status_message: str = ""

    async def start_upload(self, files: list[rx.UploadFile]):
        self.is_uploading = True
        self.status_message = "Uploading files..."
        yield

        for file in files:
            save_path = os.path.join(UPLOAD_DIR, file.filename)
            content = await file.read()

            with open(save_path, "wb") as f:
                f.write(content)

        self.status_message = "Processing documents..."
        yield

        build_vectorstore()

        self.status_message = "✅ Upload complete!"
        yield

        self.is_uploading = False
        yield

    def delete_file(self, filename: str):
        file_path = os.path.join(UPLOAD_DIR, filename)

        if os.path.exists(file_path):
            os.remove(file_path)

        build_vectorstore()


# 🔥 UI
def upload():
    return rx.vstack(

        # NAVBAR
        rx.box(
            navbar(),
            width="100%",
            box_shadow="sm",
        ),

        # MAIN CONTENT
        rx.hstack(

            # LEFT SIDE (UPLOAD)
            rx.box(
                rx.vstack(
                    rx.heading("📂 Upload Documents", size="6"),

                    rx.text(
                        "Upload PDF or TXT files and start chatting instantly.",
                        color="gray"
                    ),

                    rx.box(
                        rx.vstack(

                            # UPLOAD AREA
                            rx.upload(
                                rx.vstack(
                                    rx.text("📁 Drag & Drop files", font_size="18px", font_weight="bold"),
                                    rx.text("or click to browse", color="gray"),
                                ),
                                id="upload1",
                                border="2px dashed #94a3b8",
                                padding="50px",
                                border_radius="16px",
                                width="100%",
                                bg=rx.cond(
                                    ThemeState.color_mode == "dark",
                                    "#0f172a",
                                    "#f8fafc"
                                ),
                            ),

                            # STATUS
                            rx.cond(
                                UploadState.is_uploading,
                                rx.box(
                                    rx.hstack(
                                        rx.spinner(),
                                        rx.text(UploadState.status_message),
                                    ),
                                    padding="10px",
                                    border_radius="8px",
                                    bg=rx.cond(
                                        ThemeState.color_mode == "dark",
                                        "#1e293b",
                                        "#e0f2fe"
                                    ),
                                    width="100%",
                                )
                            ),

                            # SUCCESS MESSAGE
                            rx.cond(
                                UploadState.status_message == "✅ Upload complete!",
                                rx.text(
                                    "Files uploaded successfully 🎉",
                                    color="green",
                                    font_size="14px",
                                )
                            ),

                            # BUTTON
                            rx.button(
                                "🚀 Upload Files",
                                on_click=lambda: UploadState.start_upload(
                                    rx.upload_files(upload_id="upload1")
                                ),
                                color_scheme="blue",
                                width="100%",
                            ),

                        ),
                        padding="25px",
                        border_radius="16px",
                        bg=rx.cond(
                            ThemeState.color_mode == "dark",
                            "#1e293b",
                            "white"
                        ),
                        color=rx.cond(
                            ThemeState.color_mode == "dark",
                            "white",
                            "black"
                        ),
                        box_shadow="lg",
                        width="100%",
                    ),

                ),
                width="45%",
            ),

            # RIGHT SIDE (FILES)
            rx.box(
                rx.vstack(
                    rx.heading("📄 Uploaded Files", size="6"),

                    rx.cond(
                        len(os.listdir(UPLOAD_DIR)) == 0,
                        rx.text("No files uploaded yet 📭", color="gray"),

                        rx.vstack(
                            rx.foreach(
                                os.listdir(UPLOAD_DIR),
                                lambda file: rx.box(
                                    rx.hstack(
                                        rx.text(f"📄 {file}", font_weight="medium"),

                                        rx.spacer(),

                                        rx.text("Ready", color="green", font_size="12px"),

                                        rx.button(
                                            "Delete",
                                            color_scheme="red",
                                            size="1",
                                            variant="soft",
                                            on_click=UploadState.delete_file(file)
                                        ),
                                    ),
                                    padding="12px",
                                    border_radius="10px",
                                    bg=rx.cond(
                                        ThemeState.color_mode == "dark",
                                        "#1e293b",
                                        "white"
                                    ),
                                    color=rx.cond(
                                        ThemeState.color_mode == "dark",
                                        "white",
                                        "black"
                                    ),
                                    box_shadow="sm",
                                    width="100%",
                                ),
                            ),
                            spacing="3",
                            width="100%",
                        ),
                    ),

                ),
                width="55%",
            ),

            spacing="8",
            width="100%",
        ),

        padding="40px",
        bg=rx.cond(
            ThemeState.color_mode == "dark",
            "#0f172a",
            "#f1f5f9"
        ),
        color=rx.cond(
            ThemeState.color_mode == "dark",
            "white",
            "black"
        ),
        min_height="100vh",
        width="100%",
    )