from typing import Annotated, Optional, Union
from fastapi import Body
from pydantic import BaseModel, BeforeValidator, Field
from datetime import datetime


class Account(BaseModel):
    id: Optional[Annotated[str, BeforeValidator(str)]] = Field(alias="id", default=None)
    createdAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    updatedAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    deletedAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    softDeleted: bool = Field(...)
    active: bool = Field(...)
    lastLogin: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    role: str = Field(...)
    secret: Union[str, None] = Field(...)
    image: Union[str, None] = Field(...)
    name: Union[str, None] = Field(...)
    email: Union[str, None] = Field(...)
    phone: str = Field(...)
    document: Union[str, None] = Field(...)
    zipCode: Union[str, None] = Field(...)
    street: Union[str, None] = Field(...)
    number: Union[str, None] = Field(...)
    complement: Union[str, None] = Field(...)
    district: Union[str, None] = Field(...)
    city: Union[str, None] = Field(...)
    state: Union[str, None] = Field(...)
    latitude: Union[float, None] = Field(...)
    longitude: Union[float, None] = Field(...)


class CreateAccount(BaseModel):
    createdAt: Annotated[datetime, Body(default=datetime.now())]
    updatedAt: Annotated[datetime, Body(default=datetime.now())]
    deletedAt: Annotated[datetime, Body(default=None)]
    softDeleted: Annotated[bool, Body(default=False)]
    active: Annotated[bool, Body(default=True)]
    lastLogin: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    role: str = Annotated[str, Body()]
    secret: Annotated[str | None, Body(default=None)]
    image: Annotated[str | None, Body(default=None)]
    name: Annotated[str | None, Body(default=None)]
    email: Annotated[str | None, Body(default=None)]
    phone: str = Annotated[str, Body()]
    document: Annotated[str | None, Body(default=None)]
    zipCode: Annotated[str | None, Body(default=None)]
    street: Annotated[str | None, Body(default=None)]
    number: Annotated[str | None, Body(default=None)]
    complement: Annotated[str | None, Body(default=None)]
    district: Annotated[str | None, Body(default=None)]
    city: Annotated[str | None, Body(default=None)]
    state: Annotated[str | None, Body(default=None)]
    latitude: Annotated[float | None, Body(default=None)]
    longitude: Annotated[float | None, Body(default=None)]


class UpdateAccount(BaseModel):
    updatedAt: Annotated[datetime, Body(default=datetime.now())]
    active: Annotated[bool, Body(default=True)]
    secret: Annotated[str | None, Body(default=None)]
    image: Annotated[str | None, Body(default=None)]
    name: Annotated[str | None, Body(default=None)]
    email: Annotated[str | None, Body(default=None)]
    phone: Annotated[str | None, Body(default=None)]
    document: Annotated[str | None, Body(default=None)]
    zipCode: Annotated[str | None, Body(default=None)]
    street: Annotated[str | None, Body(default=None)]
    number: Annotated[str | None, Body(default=None)]
    complement: Annotated[str | None, Body(default=None)]
    district: Annotated[str | None, Body(default=None)]
    city: Annotated[str | None, Body(default=None)]
    state: Annotated[str | None, Body(default=None)]
    latitude: Annotated[float | None, Body(default=None)]
    longitude: Annotated[float | None, Body(default=None)]


class RemoveAccount(BaseModel):
    deletedAt: Annotated[datetime, Body(default=datetime.now())]
    active: Annotated[bool, Body(default=False)]
    softDeleted: Annotated[bool, Body(default=True)]
