import boto3

from domain.entities.product import Product
from infrastructure.repositories.i_products_repository import IProductsRepository



class DynamodbProductsRepository(IProductsRepository):
    def fetchAll(self) -> list[Product]:
        table = boto3.resource("dynamodb").Table("Products")
        response = table.scan()
        items = response["Items"]
        products = []
        for product in items:
            products.append(
                Product(
                    product["name"],
                    float(product["price"]),
                    int(product["quantity"]))
                )
        
        return products
