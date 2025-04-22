import reflex as rx 
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.link(
            f"© 2025-{datetime.date.today().year} NO CRUSH WEB BY MIGUEL AGUILAR", 
            href="https://www.instagram.com/miguel.ang.lagunas/",
            is_external=True
        ),
        align="center"
    )
