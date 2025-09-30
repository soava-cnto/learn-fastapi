from fastapi import HTTPException, status


def product_not_found(product_id: int):
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = f"Produit avec id={product_id} non trouvé"
    )    
    
def no_products():
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = f"Plus de produits "
    )