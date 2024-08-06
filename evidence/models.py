from typing import Annotated, Optional, Union
from fastapi import Body
from pydantic import BaseModel, BeforeValidator, Field
from datetime import datetime


class Evidence(BaseModel):
    id: Optional[Annotated[str, BeforeValidator(str)]] = Field(alias="id", default=None)
    createdAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    updatedAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    deletedAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    softDeleted: bool = Field(...)
    active: bool = Field(...)
    code: str = Field(...)
    note: Union[str, None] = Field(...)
    file: Union[str, None] = Field(...)
    orderId: Annotated[str, BeforeValidator(str)] = Field(...)


class CreateEvidence(BaseModel):
    createdAt: Annotated[datetime, Body(default=datetime.now())]
    updatedAt: Annotated[datetime, Body(default=datetime.now())]
    deletedAt: Annotated[datetime, Body(default=None)]
    softDeleted: Annotated[bool, Body(default=False)]
    active: Annotated[bool, Body(default=True)]
    code: Annotated[str, Body(min_length=8, max_length=12)]
    note: Annotated[str | None, Body(default=None)]
    file: Annotated[str | None, Body(default=None)]
    orderId: Annotated[str, Body()]


class UpdateEvidence(BaseModel):
    updatedAt: Annotated[datetime, Body(default=datetime.now())]
    active: Annotated[bool, Body(default=True)]
    note: Annotated[str | None, Body(default=None)]
    file: Annotated[str | None, Body(default=None)]


class RemoveEvidence(BaseModel):
    deletedAt: Annotated[datetime, Body(default=datetime.now())]
    active: Annotated[bool, Body(default=False)]
    softDeleted: Annotated[bool, Body(default=True)]
