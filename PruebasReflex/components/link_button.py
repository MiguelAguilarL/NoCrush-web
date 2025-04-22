import reflex as rx
import PruebasReflex.styles.styles as styles
from PruebasReflex.styles.styles import Size

def link_button(title: str, body: str, image: str, link: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.BIG.value,
                    height=Size.BIG.value,
                    margin=Size.MEDIUM.value,
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing="1",
                    margin=Size.ZERO.value,
                ),
                align="center"
            )
        ), 
        href=link, 
        is_external=True,
        width="100%"
    )
