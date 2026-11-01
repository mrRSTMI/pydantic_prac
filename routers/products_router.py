from fastapi import APIRouter, HTTPException, status
from schemas.products_schema import ProductResponse

router = APIRouter(prefix="/api/product", tags=["Products"])



@router.get("/all-products", response_model=ProductResponse)
def get_all_products():
    return {"all products"}
