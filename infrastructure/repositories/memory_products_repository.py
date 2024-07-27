from domain.entities.product import Product
from infrastructure.repositories.i_products_repository import IProductsRepository



class MemoryProductsRepository(IProductsRepository):
    def __init__(self) -> None:
        self.products = [
            Product("Product 1", 10.99, 100),
            Product("Product 2", 20.99, 200),
            Product("Product 3", 30.99, 300),
        ]

    def fetchAll(self) -> list[Product]:
        return self.products
