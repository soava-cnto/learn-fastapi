from fastapi import FastAPI
from routes import products


app = FastAPI()

app.include_router(products.router, prefix="/products", tags=["Produits"])