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
)


class OrderCreate(BaseModel):
    pass


class OrderResponse(BaseModel):
    pass
