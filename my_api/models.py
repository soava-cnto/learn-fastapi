from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    in_stock: bool = True