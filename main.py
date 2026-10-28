from fastapi import FastAPI, HTTPException, status
from products_schema import ProductCreater, ProductResponse, ProductUpdate

# creating app
app = FastAPI(title="prac pydantic")


products_db = {
    1: {
        "id": 1,
        "name": "Keyboard",
        "price": 49.99,
        "quantity": 5,
    }
}


@app.get("/")
def message_hello():
    return {"message": "hello world !!!"}


@app.post("/create-product", response_model=ProductResponse)
def create_products(products: ProductCreater):
    return {"id": 101, **products.model_dump()}


@app.patch("/update-product/{product_id}")
def update_product(product_id: int, update: ProductUpdate):
    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"product not found by id: {product_id}",
        )
    change_product = update.model_dump(exclude_unset=True)
    products_db[product_id].update(change_product)
    return products_db[product_id]
