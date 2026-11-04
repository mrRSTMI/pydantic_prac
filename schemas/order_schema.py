from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
    PositiveInt,
    PositiveFloat,
    EmailStr,
    ConfigDict,
)


class BaseOrderModel(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )


class Customer(BaseOrderModel):
    name: str = Field(min_length=3)
    email: EmailStr


class Address(BaseOrderModel):
    city: str = Field(min_length=2)
    street: str = Field(min_length=3)
    postal_code: str = Field(min_length=10, max_length=10)


class OrderItem(BaseOrderModel):
    product_id: PositiveInt
    quantity: PositiveInt


class OrderCreate(BaseOrderModel):
    customer: Customer
    address: Address
    items: list[OrderItem]

    @field_validator("items")
    @classmethod
    def validate_items(cls, value):
        # if not value or
        if len(value) == 0:
            raise ValueError("order just be 1 item or more !!!")
        return value


class OrderResponse(BaseOrderModel):
    id: PositiveInt
    customer: Customer
    address: Address
    items: list[OrderItem]
    total_price: PositiveFloat
