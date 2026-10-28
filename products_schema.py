from pydantic import BaseModel, Field, ConfigDict, TypeAdapter

class ProductCreater(BaseModel):
    name:str = Field(min_length=2, max_length=50)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0, default=0)

class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=0, max_length=50)
    price: float | None = Field(default=None, gt=0)
    quantity: int | None = Field(default=None,ge=0)

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    quantity: int