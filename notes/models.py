from typing import Annotated, Optional, Union
from fastapi import Body
from pydantic import BaseModel, BeforeValidator, Field
from datetime import datetime


class Note(BaseModel):
    id: Optional[Annotated[str, BeforeValidator(str)]] = Field(alias="id", default=None)
    createdAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    updatedAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    deletedAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    softDeleted: bool = Field(...)
    active: bool = Field(...)
    code: str = Field(...)
    reference: str = Field(...)
    topic: Union[str, None] = Field(...)
    content: Union[str, None] = Field(...)


class CreateNote(BaseModel):
    createdAt: Annotated[datetime, Body(default=datetime.now())]
    updatedAt: Annotated[datetime, Body(default=datetime.now())]
    deletedAt: Annotated[datetime, Body(default=None)]
    softDeleted: Annotated[bool, Body(default=False)]
    active: Annotated[bool, Body(default=False)]
    code: Annotated[str, Body(min_length=8, max_length=12)]
    reference: Annotated[str, Body(min_length=8, max_length=14)]
    topic: Annotated[str | None, Body(default=None)]
    content: Annotated[str | None, Body(default=None)]


class UpdateNote(BaseModel):
    updatedAt: Annotated[datetime, Body(default=datetime.now())]
    active: Annotated[bool, Body(default=False)]
    topic: Annotated[str | None, Body(default=None)]
    content: Annotated[str | None, Body(default=None)]


class RemoveNote(BaseModel):
    deletedAt: Annotated[datetime, Body(default=datetime.now())]
    active: Annotated[bool, Body(default=False)]
    softDeleted: Annotated[bool, Body(default=True)]
