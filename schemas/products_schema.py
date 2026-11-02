from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
    PositiveFloat,
    PositiveInt,
    EmailStr,
    HttpUrl,
    ConfigDict,
    NonNegativeInt,
)


class BaseProductsModel(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")


class Category(BaseProductsModel):
    name_category: str


class ProductCreate(BaseProductsModel):
    product_name: str = Field(min_length=3, max_length=50)
    price: PositiveFloat
    quantity: NonNegativeInt
    category: Category
    website: HttpUrl


class ProductUpdate(BaseProductsModel):
    product_name: str | None = Field(min_length=3, max_length=50, default=None)
    price: PositiveFloat | None = Field(default=None)
    quantity: NonNegativeInt | None = Field(default=None)
    category: Category | None = Field(default=None)
    website: HttpUrl | None = Field(default=None)


class ProductResponse(BaseProductsModel):
    id: PositiveInt
    product_name: str
    price: PositiveFloat
    quantity: NonNegativeInt
    category: Category
