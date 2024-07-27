from infrastructure.repositories.i_products_repository import IProductsRepository


class FetchProductsUseCase:
    def __init__(self, product_repository: IProductsRepository):
        self.product_repository = product_repository

    def  execute(self):
        return self.product_repository.fetchAll()
