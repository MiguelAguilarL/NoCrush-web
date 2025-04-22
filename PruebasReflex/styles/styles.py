import reflex as rx
from enum import Enum
from PruebasReflex.styles.colors import Color as Color
from PruebasReflex.styles.colors import TextColor as TextColor

MAX_WIDTH = "600px"

class Size(Enum):
    ZERO = "0em !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "em"
    LARGE = "1.5em"
    BIG = "2em"

BASE_STYLE = {
    "margin": "0",
    "background_image": "url('background.png')",
    "background_size": "cover",
    "background-attachment": "scroll",
    "background_position": "center",
    "background_color": Color.BACKGROUND.value,
    rx.button: {
        "background_color": Color.CONTENT.value,
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.LARGE.value,
        "_hover": {
            "background_color": Color.SECONDARY.value,
            "transition": "background 1s ease"
        }
    }
}

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
)

button_title_style = dict(
    font_size = Size.DEFAULT.value,
    color = TextColor.HEADER.value
)

button_body_style = dict(
    font_size = Size.MEDIUM.value,
    color = TextColor.BODY.value
)