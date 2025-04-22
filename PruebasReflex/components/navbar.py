import reflex as rx
from PruebasReflex.styles.styles import Size as Size
from PruebasReflex.styles.colors import Color as Color


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "ＮＯ  ＣＲＵＳＨ!",
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0"
    )