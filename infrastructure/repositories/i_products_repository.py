from abc import ABC, abstractmethod

from domain.entities.product import Product

class IProductsRepository(ABC):
    @abstractmethod
    def fetchAll(self) -> list[Product]:
        pass
