import azure.functions as func
from azure.cosmos import CosmosClient
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.route_params.get("id")

    client = CosmosClient(os.getenv("COSMOS_URI"), credential=os.getenv("COSMOS_KEY"))
    container = client.get_database_client(os.getenv("COSMOS_DB")).get_container_client(os.getenv("COSMOS_CONTAINER"))

    try:
        container.delete_item(id, id)
        return func.HttpResponse(status_code=204)
    except:
        return func.HttpResponse("Not Found", status_code=404)
