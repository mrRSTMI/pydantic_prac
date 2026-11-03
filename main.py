from fastapi import FastAPI, HTTPException, status
from schemas.products_schema import ProductCreate, ProductResponse, ProductUpdate
from routers.products_router import product_router

app = FastAPI(title="Product API")
app.include_router(router=product_router)
