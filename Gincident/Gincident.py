"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from Gincident.models import Referents, SessionLocal

print("packages successfully imported")
print("===============================================")


print(type(Referents))
print("===============================================")

class State(rx.State):
    logged_in = False
    user_role = None
    username = ""

    @staticmethod
    def login(email, password):
        session = SessionLocal()
        user = session.query(Referents).filter_by(email=email).first()
        if user and user.mot_de_passe == password:
            State.logged_in = True
            State.user_role = user.role
            State.username = f"{user.nom} {user.prenom}"
        else:
            State.logged_in = False
        session.close()

    @staticmethod
    def logout():
        State.logged_in = False
        State.user_role = None
        State.username = ""

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="/login_page",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )



def login_page():
    return rx.center(
        rx.vstack(
            rx.input(placeholder="Email", id="email"),
            rx.input(placeholder="Mot de passe", type_="password", id="password"),
            rx.button(
                "Connexion",
                on_click=lambda: State.login(rx.get_state("email"), rx.get_state("password")),
            ),
            rx.cond(State.logged_in, rx.redirect("/dashboard")),
        )
    )

def dashboard():
    return rx.cond(
        State.logged_in,
        rx.center(
            rx.vstack(
                rx.heading(f"Bienvenue, {State.username}"),
                rx.cond(State.user_role == "admin", rx.text("Vous êtes un administrateur.")),
                rx.link("Gérer les incidents", href="/incidents"),
                rx.link("Gérer les actions", href="/actions"),
                rx.link("Cartographie", href="/map"),
                rx.button("Déconnexion", on_click=State.logout),
            )
        ),
        rx.redirect("/login"),
    )


def incidents():
    return rx.center(
        rx.vstack(
            rx.heading("Gestion des incidents"),
            rx.input(placeholder="Type d'incident"),
            rx.input(placeholder="Niveau de risque (1-10)", type_="number"),
            rx.input(placeholder="Localisation"),
            rx.button("Ajouter l'incident", on_click=lambda: print("Incident ajouté")),
            rx.link("Retour au tableau de bord", href="/dashboard"),
        )
    )


def actions():
    return rx.center(
        rx.vstack(
            rx.heading("Gestion des actions"),
            rx.input(placeholder="Intitulé de l'action"),
            rx.input(placeholder="Date limite", type_="date"),
            rx.button("Ajouter l'action", on_click=lambda: print("Action ajoutée")),
            rx.link("Retour au tableau de bord", href="/dashboard"),
        )
    )


def map_page():
    return rx.center(
        rx.text("Carte des incidents (à intégrer avec une API comme Leaflet ou Google Maps).")
    )



app = rx.App()
app.add_page(index)
app.add_page(login_page, route="/login")
app.add_page(dashboard, route="/dashboard")
app.add_page(incidents, route="/incidents")
app.add_page(actions, route="/actions")
app.add_page(map_page, route="/map")
app.compile()
