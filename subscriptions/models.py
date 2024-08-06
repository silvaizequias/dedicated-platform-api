from typing import Annotated, Optional, Union
from fastapi import Body
from pydantic import BaseModel, BeforeValidator, Field
from datetime import datetime


class Subscription(BaseModel):
    id: Optional[Annotated[str, BeforeValidator(str)]] = Field(alias="id", default=None)
    createdAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    updatedAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    deletedAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    softDeleted: bool = Field(...)
    active: bool = Field(...)
    credit: int = Field(...)
    unlimited: bool = Field(...)
    paymentGateway: Union[str, None] = Field(...)
    customerId: Union[str, None] = Field(...)
    accountId: str = Field(...)


class CreateSubscription(BaseModel):
    createdAt: Annotated[datetime, Body(default=datetime.now())]
    updatedAt: Annotated[datetime, Body(default=datetime.now())]
    deletedAt: Annotated[datetime, Body(default=None)]
    softDeleted: Annotated[bool, Body(default=False)]
    active: Annotated[bool, Body(default=False)]
    code: Annotated[str, Body(min_length=8, max_length=12)]
    credit: Annotated[int, Body(default=100)]
    unlimited: Annotated[bool, Body(default=False)]
    paymentGateway: Annotated[str, Body(min_length=8, max_length=12, default=None)]
    customerId: Annotated[str | None, Body(default=None)]
    accountId: Annotated[str, Body()]


class UpdateSubscription(BaseModel):
    updatedAt: Annotated[datetime, Body(default=datetime.now())]
    active: Annotated[bool, Body(default=False)]
    credit: Annotated[int, Body(default=100)]
    unlimited: Annotated[bool, Body(default=False)]
    paymentGateway: Annotated[str | None, Body(min_length=8, max_length=12, default=None)]
    customerId: Annotated[str | None, Body(default=None)]


class RemoveSubscription(BaseModel):
    deletedAt: Annotated[datetime, Body(default=datetime.now())]
    active: Annotated[bool, Body(default=False)]
    softDeleted: Annotated[bool, Body(default=True)]
