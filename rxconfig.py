import reflex as rx

config = rx.Config(
    app_name="DOCU_AI",
    #api_url="https://f5613b0f-9da9-4cd8-a31a-25cfd99f2037.fly.dev",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)