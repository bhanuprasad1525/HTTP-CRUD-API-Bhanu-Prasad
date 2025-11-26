# Azure Functions – CosmosDB CRUD API

This project is a Serverless CRUD API built using Azure Functions (Python) integrated with Azure Cosmos DB.
It exposes REST APIs to Create, Read, Update and Delete Products in Cosmos DB.

Tech Stack :
- Backend	- Azure Functions (Python)
- Database -	Azure Cosmos DB (SQL API)
- Language -	Python 3.10
- Runtime	Azure Functions v4
- Tools -	Thunder Client
- Hosting	Azure Function App

Features

- Create Product
- List All Products
- Get Product By ID
- Update Product
- Delete Product

Environment Variables

- COSMOS_URI
- COSMOS_KEY
- COSMOS_DB
- COSMOS_CONTAINER

API Endpoints (Local)

- Create Product -	    POST	 -  http://localhost:7071/api/products
- List Products -	      GET	   -  http://localhost:7071/api/products
- Get Product By ID - 	GET	   -  http://localhost:7071/api/products/{id}
- Update Product -	    PUT	   -  http://localhost:7071/api/products/{id}
- Delete Product -	    DELETE -	http://localhost:7071/api/products/{id}

Sample Request Body

 POST - Create Product :
{
  "id": "p101",
  "name": "Keyboard",
  "price": 399.00
}

 PUT - Update Product :
{
  "price": 499.00
}

Responses
- Successful Create :  201 CREATED
- Successful Update :  200 UPDATED
- Successful Delete :  204 NO CONTENT
- Not Found         :  404 NOT FOUND

Cosmos DB Partition Key : /id

Deployment Steps:
- func azure functionapp publish task21 --build remote

Status : All 5 endpoints tested successfully using Thunder Client.

NOTE :

- Azure CosmosDB  Name :  bhanucosmos21
- FunctionApp     Name  :  task21
  
