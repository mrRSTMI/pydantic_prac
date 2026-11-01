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


class Address(BaseModel):
    pass


class UserCreate(BaseModel):
    pass
