from fastapi import FastAPI
from pydantic import BaseModel   # Pour créer des modèles de données

app = FastAPI()

# --- Définition d'un modèle Pydantic ---
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True   # Valeur par défaut

# --- Endpoint pour créer un utilisateur ---
@app.post("/users/")
def create_user(user: User):
    """
    Cette fonction reçoit un objet JSON qui sera validé par le modèle User.
    FastAPI convertit automatiquement le JSON en objet 'User'.
    """
    
    return {
        "message": "Utilisateur créé avec succès ✅",
        "data": user
    }
