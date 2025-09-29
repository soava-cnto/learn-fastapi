from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# --- Modèle Produit ---
class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

# --- Base de données simulée (en mémoire) ---
products = []

# --- Route GET : liste des produits ---
@app.get("/products/")
def get_products():
    return {"products": products}

# --- Route POST : ajouter un produit ---
@app.post("/products/")
def add_product(product: Product):
    products.append(product)
    return {"message": "Produit ajouté ✅", "data": product}
