import reflex as rx
from rxconfig import config
from PruebasReflex.components.navbar import navbar
from PruebasReflex.views.header.header import header
from PruebasReflex.views.links.links import links
from PruebasReflex.components.footer import footer
import PruebasReflex.styles.styles as styles
from PruebasReflex.styles.styles import Size

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.LARGE.value,
                align="center"
            )
        ),
        footer()
    )


app = rx.App(
    style=styles.BASE_STYLE,
)
app.add_page(
    index,
    title="No Crush! | Web Oficial"
    )
