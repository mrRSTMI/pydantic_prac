from fastapi import APIRouter, HTTPException, status
from schemas.products_schema import ProductResponse, ProductCreate, ProductUpdate
from database.data import products

product_router = APIRouter(prefix="/api/product", tags=["Products"])


@product_router.get("/all-products", response_model=list[ProductResponse])
def get_all_products():
    return products


@product_router.get("/product/{product_id:int}", response_model=ProductResponse)
def get_product_by_id(product_id: int):
    for p in products:
        if p["id"] == product_id:
            return p

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"prodcut by id: {product_id} not found",
    )


@product_router.post(
    "/new-product",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_product(product: ProductCreate):
    new_product = {"id": len(products) + 1, **product.model_dump()}
    products.append(new_product)
    return new_product


@product_router.patch(
    "/update-product/{product_id:int}", response_model=ProductResponse
)
def update_prodcut_by_id(product_id: int, updating_product: ProductUpdate):
    for product in products:
        if product["id"] == product_id:
            product.update(updating_product.model_dump(exclude_unset=True))
            return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"product by id: {product_id} not found !!!",
    )


@product_router.delete(
    "/delete-product/{id_deleted:int}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_product_by_id(id_deleted: int):
    for p in products:
        if p["id"] == id_deleted:
            products.remove(p)
            return {
                "message": f"product is deleted!!!",
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"product by id: {id_deleted} not found ! ! !",
    )
