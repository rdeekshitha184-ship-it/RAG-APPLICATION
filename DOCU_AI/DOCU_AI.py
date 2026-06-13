import reflex as rx

from DOCU_AI.pages.about import about
from DOCU_AI.pages.home import home
from DOCU_AI.pages.upload import upload
from DOCU_AI.pages.chat import chat
from DOCU_AI.pages.history import history

app = rx.App()

app.add_page(home, route="/")
app.add_page(upload, route="/upload")
app.add_page(chat, route="/chat")
app.add_page(history, route="/history")
app.add_page(about, route="/about")
