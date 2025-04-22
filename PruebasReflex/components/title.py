import reflex as rx
import PruebasReflex.styles.styles as styles


def title(text: str, position = "left", sz="8") -> rx.Component:
    return rx.heading(text, size=sz, align=position, style=styles.title_style)