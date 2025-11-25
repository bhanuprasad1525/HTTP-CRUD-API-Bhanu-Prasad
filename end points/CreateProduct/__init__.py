import azure.functions as func
from azure.cosmos import CosmosClient
import os
import json

def main(req: func.HttpRequest) -> func.HttpResponse:

    client = CosmosClient(os.getenv("COSMOS_URI"), credential=os.getenv("COSMOS_KEY"))
    container = client.get_database_client(os.getenv("COSMOS_DB")).get_container_client(os.getenv("COSMOS_CONTAINER"))

    body = req.get_json()

    container.create_item(body)

    return func.HttpResponse("Created", status_code=201)
