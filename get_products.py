import json

from application.use_cases.fetch_products_use_case import FetchProductsUseCase
from infrastructure.repositories.i_products_repository import IProductsRepository
from infrastructure.repositories.dynamodb_products_repository import DynamodbProductsRepository


def lambda_handler(event, context) -> dict:
    products_repo = DynamodbProductsRepository()
    
    return execute(event, products_repo)

def execute(event: str, products_repo: IProductsRepository) -> dict:
    use_case = FetchProductsUseCase(products_repo)
    
    return {
        "statusCode": 200,
        "headers": {},
        "body": json.dumps([ob.__dict__ for ob in use_case.execute()])
    }
