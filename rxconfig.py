import reflex as rx

config = rx.Config(
    app_name="DOCU_AI",
    api_url="https://docu-ai-bjrt.onrender.com",
    backend_port=8000,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)