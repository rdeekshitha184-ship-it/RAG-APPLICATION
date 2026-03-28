import reflex as rx

class ThemeState(rx.State):
    color_mode: str = "light"

    def toggle_theme(self):
        self.color_mode = "dark" if self.color_mode == "light" else "light"