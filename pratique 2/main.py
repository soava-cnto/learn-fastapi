from fastapi import FastAPI

app = FastAPI()

# --- Exemple 1 : Path Parameter ---
@app.get("/users/{user_id}")
def lire_utilisateur(user_id: int):
    # user_id sera automatiquement converti en int (grâce à la "type int" int)
    return {"user_id": user_id, "message": f"Utilisateur numéro {user_id}"}


# --- Exemple 2 : Query Parameter ---
@app.get("/items/")
def lire_items(q: str = None, limit: int = 10):
    # q est optionnel (par défaut None), limit a une valeur par défaut = 10
    return {"query": q, "limit": limit}
