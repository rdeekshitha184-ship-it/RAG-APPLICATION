
import reflex as rx

def navbar():
    return rx.box(
        rx.hstack(
            rx.text("DocuAI", font_size="24px", font_weight="bold", color="white"),

            rx.spacer(),

            rx.hstack(
                rx.link("Home", href="/"),
                rx.link("UploadDocument", href="/upload"),
                rx.link("Chat", href="/chat"),
                rx.link("ChatHistory", href="/history"),
                rx.link("About", href="/about"),
                spacing="5",
                color="white"
            ),
            width="100%",
            padding="15px"
        ),
        width="100%",
        bg="linear-gradient(to right, #4facfe, #00f2fe)",
        margin="0",
        padding="0"
    )
