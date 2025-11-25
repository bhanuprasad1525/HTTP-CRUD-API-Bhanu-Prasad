import azure.functions as func
from azure.cosmos import CosmosClient
import os, json

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.route_params.get("id")
    body = req.get_json()

    client = CosmosClient(os.getenv("COSMOS_URI"), credential=os.getenv("COSMOS_KEY"))
    container = client.get_database_client(os.getenv("COSMOS_DB")).get_container_client(os.getenv("COSMOS_CONTAINER"))

    try:
        item = container.read_item(id, id)
    except:
        return func.HttpResponse("Not Found", status_code=404)

    for k,v in body.items():
        item[k] = v

    container.replace_item(id, item)

    return func.HttpResponse("Updated", status_code=200)
