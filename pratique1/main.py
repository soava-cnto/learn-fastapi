from fastapi import FastAPI   # On importe FastAPI depuis la librairie fastapi

app = FastAPI()               # On crée une instance de l'application FastAPI

@app.get("/")                 # On définit une route GET sur "/"
def home():                   # Fonction associée à la route
    return {"message": "Bienvenue sur mon API 🚀"}   # Réponse JSON

@app.get("/hello/{nom}")      # On définit une route GET dynamique avec un paramètre "nom"
def dire_bonjour(nom: str):   # La fonction reçoit "nom" comme paramètre (type string)
    return {"message": f"Salut {nom}, bienvenue dans FastAPI !"}  # Réponse JSON
