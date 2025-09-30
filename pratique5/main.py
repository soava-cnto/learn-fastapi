from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
from fastapi import status



app = FastAPI()


class Product(BaseModel):
    name: str
    price: float
    in_stock: bool = True

products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Smartphone", "price": 800},
]

@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: Product):
    new_product = product.dict()
    new_product["id"] = len(products) + 1    
    products.append(new_product)
    return {"message": "Produit ajouté ✅", "product": new_product}

@app.get("/products")
def get_products():
    return {"products": products}

@app.get("/products/{product_id}", status_code=status.HTTP_200_OK)
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Produit non trouvé")

@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            products[index].update(updated_product.dict())
            return {"message": "Produit mis à jour ✅", "product": products[index]}
    
    raise HTTPException(status_code=404, detail="Produit non trouvé")

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            deleted = products.pop(index)
            return {"message": "Produit supprimé 🗑️", "product": deleted}
    
    raise HTTPException(status_code=404, detail="Produit non trouvé")
