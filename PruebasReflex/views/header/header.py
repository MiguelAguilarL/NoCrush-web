import reflex as rx
from PruebasReflex.components.title import title
from PruebasReflex.styles.colors import TextColor
from PruebasReflex.styles.colors import Color
from PruebasReflex.styles.styles import Size

def header() -> rx.Component:
    return rx.vstack(  
        rx.hstack(
        rx.avatar(
            src="/buxxy.jpg", 
            radius="full", 
            padding="2px",
            border="4px",
            border_style="solid",
            border_color="#147ddb",
            size="8"
        ),
        rx.vstack(
            title("No Crush!", "center"),
        ),
            align="center",
        ),
    rx.text("""¡Bienvenido/a a la página oficial de No Crush! Aquí podrás encontrar todos 
                nuestros enlaces de interés. No olvides de seguirnos en todas nuestras redes 
                sociales para estar al tanto de nueva información y lanzamientos próximos. Próximo 
                sencillo "I Left The Life Before I Die" disponible muy pronto en todas las plataformas.""",
                background_color=Color.CONTENT,
                color=TextColor.BODY.value,
                width= "100%",
                height= "100%",
                display= "block",
                padding= Size.SMALL.value,
                border_radius= Size.LARGE.value,
            ),
    align_items="start",
    align="center"
    )   
    