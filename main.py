from fastapi import FastAPI, HTTPException, status
from schemas.products_schema import ProductCreate, ProductResponse, ProductUpdate

app = FastAPI(title="Product API")




@app.post("/create-products", response_model=ProductResponse)
def create_product(product: ProductCreate):
    pass


@app.patch("/update-product/{product_id:int}", response_model=ProductResponse)
def update_product_by_id(product_id: int, product: ProductUpdate):
    pass


@app.delete("delete-product/{product_id:int}", response_model=ProductResponse)
def delete_product_by_id(product_id: int):
    pass
