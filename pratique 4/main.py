from fastapi import FastAPI
from typing import Optional
from fastapi import Query

app = FastAPI()

# 📦 Exemple de base de données fictive
products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Smartphone", "price": 800},
    {"id": 3, "name": "Clavier", "price": 50},
    {"id": 4, "name": "Souris", "price": 30},
]

# ✅ Route GET pour récupérer tous les produits
@app.get("/products")
def get_products():
    return {"products": products}


# ✅ Path parameter → chercher un produit par son ID
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Produit non trouvé"}


# ✅ Query parameter → filtrer les produits par prix max
@app.get("/filter_products/")
def filter_products(max_price: Optional[int] = None): # pas obligatoire ici avec optional
# def filter_products(max_price: int = Query(...)): # obligatoire
    if max_price is None:
        return {"products": products}
    filtered = [p for p in products if p["price"] <= max_price]
    return {
        "products": filtered,
        "total": len(filtered)
        }
