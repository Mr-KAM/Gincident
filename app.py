import reflex as rx
from pages.login import login_page
from pages.dashboard import dashboard
from pages.incidents import incidents
from pages.actions import actions
from pages.map import map_page
from state import State

# Créer une instance de l'application Reflex
app = rx.App()

# Ajouter les pages principales
app.add_page(login_page, route="/login")
app.add_page(dashboard, route="/dashboard")
app.add_page(incidents, route="/incidents")
app.add_page(actions, route="/actions")
app.add_page(map_page, route="/map")

# Ajouter une page par défaut (exemple : rediriger vers le tableau de bord si connecté)
@app.on_start
def set_default_page():
    if State.logged_in:
        return rx.redirect("/dashboard")
    return rx.redirect("/login")

# Compiler l'application
app.compile()
