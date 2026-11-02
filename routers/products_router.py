from fastapi import APIRouter, HTTPException, status
from schemas.products_schema import ProductResponse, ProductCreate, ProductUpdate
from database.data import products

router = APIRouter(prefix="/api/product", tags=["Products"])


@router.get("/all-products", response_model=ProductResponse)
def get_all_products():
    return products


@router.get("/product/{product_id:int}", response_model=ProductResponse)
def get_product_by_id(product_id: int):
    if not product_id in products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"prodcut by id: {product_id} not found",
        )
    return products[product_id]


@router.post("/new-product", response_model=ProductResponse)
def create_product(product: ProductCreate):
    new_product = {id: len(products) + 1, **product.model_dump()}
    products.append(new_product)
    return new_product


@router.patch("/update-product/{product_id:int}", response_model=ProductResponse)
def update_prodcut_by_id(product_id: int, updating_product: ProductUpdate):
    if not product_id in products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"product by id: {product_id} not found !!!",
        )
    for product in products:
        if product_id == product.id:
            product.update(**updating_product)
            return product
