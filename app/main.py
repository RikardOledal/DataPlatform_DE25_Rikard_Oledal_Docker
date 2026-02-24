from fastapi import FastAPI
from app.schema.Product import ProductSchema
from starlette import status

app = FastAPI(title="Lektion9")

@app.get("/")
def root():
    return {"message": "Hello world"}

@app.post("/products", status_code=status.HTTP_201_CREATED, response_model=ProductSchema)
def post_product(product: ProductSchema) -> ProductSchema:

    return product