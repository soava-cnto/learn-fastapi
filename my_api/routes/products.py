from fastapi import APIRouter, status
from models import Product
from exceptions import product_not_found, no_products
from typing import Optional


router = APIRouter()

products = []

@router.get("/", status_code = status.HTTP_200_OK)
def get_products():
    return {
        "products": products,
        "total": len(products)
        }

@router.post("/", status_code = status.HTTP_201_CREATED)
def create_product(product: Product):
    new_product =  product.dict()
    new_product["id"] = len(products) + 1
    products.append(new_product)
    return {
        "message": "Produit ajouté ✅",
        "produit": new_product
    }
    
@router.get("/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    product_not_found(product_id)
    
@router.put("/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            products[index].update(updated_product.dict())
            return {
                "message": "Produit mis à jour ✅", 
                "product": products[index] 
            }
    product_not_found(product_id)
    
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            products.pop(index)
            return 
    product_not_found(product_id)

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_all_products():
    if len(products) > 0:
        products.clear()    
        return {"message": "Tous les produits ont été supprimés"}
    no_products()
    
@router.get("/filter/", status_code=status.HTTP_200_OK)
def filter_product_by_price(price_max: Optional[int] = None):
    if not products:
        no_products()
        
    if price_max is None:
        return {"products": products, "total": len(products)}
    
    filtered = [p for p in products if p["price"] <= price_max]
    return {"products": filtered, "total": len(filtered)}

