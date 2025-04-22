import reflex as rx
from PruebasReflex.components.link_button import link_button
from PruebasReflex.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Síguenos", "left", "7"),
        link_button(
            "Spotify", 
            "Escucha nuestras canciones en Spotify",
            "/icons/spotify.svg",
            "https://open.spotify.com/artist/0MI3YHe7eRw6jQyRoJqKS8"
            ),
        link_button(
            "Instagram", 
            "Siguenos en Instagram",
            "/icons/instagram.svg",
            "https://www.instagram.com/nocrush_.official/"
            ),
        link_button(
            "YouTube", 
            "Nuestro YouTube oficial",
            "/icons/youtube.svg",
            "https://www.youtube.com/channel/UC-8ou4HJVYi745XEG6C1cbw"),
        title("Contacto", "left", "7"),
        link_button(
            "Email", 
            "Nuestro correo",
            "/icons/mail.svg",
            "mailto:mikeal2123495@gmail.com",
        ),
        width="100%",
        align="center"
        )