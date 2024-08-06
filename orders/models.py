from typing import Annotated, Optional, Union
from fastapi import Body
from pydantic import BaseModel, BeforeValidator, Field
from datetime import datetime


class Order(BaseModel):
    id: Optional[Annotated[str, BeforeValidator(str)]] = Field(alias="id", default=None)
    createdAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    updatedAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    deletedAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    softDeleted: bool = Field(...)
    active: bool = Field(...)
    code: str = Field(...)
    barCode: Union[str, None] = Field(...)
    serial: Union[str, None] = Field(...)
    control: Union[str, None] = Field(...)
    topic: Union[str, None] = Field(...)
    description: Union[str, None] = Field(...)
    issuer: Union[str, None] = Field(...)
    customer: Union[str, None] = Field(...)
    status: str = Field(...)


class CreateOrder(BaseModel):
    createdAt: Annotated[datetime, Body(default=datetime.now())]
    updatedAt: Annotated[datetime, Body(default=datetime.now())]
    deletedAt: Annotated[datetime, Body(default=None)]
    softDeleted: Annotated[bool, Body(default=False)]
    active: Annotated[bool, Body(default=False)]
    code: Annotated[str, Body(min_length=8, max_length=12)]
    barCode: Annotated[str | None, Body(default=None)]
    serial: Annotated[str | None, Body(default=None)]
    control: Annotated[str | None, Body(default=None)]
    topic: Annotated[str | None, Body(default=None)]
    description: Annotated[str | None, Body(default=None)]
    issuer: Annotated[str | None, Body(default=None, min_length=11, max_length=14)]
    customer: Annotated[str | None, Body(default=None, min_length=11, max_length=14)]
    status: Annotated[str, Body()]


class UpdateOrder(BaseModel):
    updatedAt: Annotated[datetime, Body(default=datetime.now())]
    active: Annotated[bool, Body(default=False)]
    barCode: Annotated[str | None, Body(default=None)]
    serial: Annotated[str | None, Body(default=None)]
    control: Annotated[str | None, Body(default=None)]
    topic: Annotated[str | None, Body(default=None)]
    description: Annotated[str | None, Body(default=None)]
    issuer: Annotated[str | None, Body(default=None, min_length=11, max_length=14)]
    customer: Annotated[str | None, Body(default=None, min_length=11, max_length=14)]
    status: Annotated[str | None, Body(default=None)]


class RemoveOrder(BaseModel):
    deletedAt: Annotated[datetime, Body(default=datetime.now())]
    active: Annotated[bool, Body(default=False)]
    softDeleted: Annotated[bool, Body(default=True)]
