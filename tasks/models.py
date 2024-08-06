from typing import Annotated, Optional, Union
from fastapi import Body
from pydantic import BaseModel, BeforeValidator, Field
from datetime import datetime


class Task(BaseModel):
    id: Optional[Annotated[str, BeforeValidator(str)]] = Field(alias="id", default=None)
    createdAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    updatedAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    deletedAt: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    softDeleted: bool = Field(...)
    active: bool = Field(...)
    code: str = Field(...)
    reference: Union[str, None] = Field(...)
    topic: Union[str, None] = Field(...)
    subject: Union[str, None] = Field(...)
    description: Union[str, None] = Field(...)
    deadline: Optional[Annotated[str, BeforeValidator(str)]] = Field(default=None)
    status: str = Field(...)
    owner: Union[str, None] = Field(...)


class CreateTask(BaseModel):
    createdAt: Annotated[datetime, Body(default=datetime.now())]
    updatedAt: Annotated[datetime, Body(default=datetime.now())]
    deletedAt: Annotated[datetime, Body(default=None)]
    softDeleted: Annotated[bool, Body(default=False)]
    active: Annotated[bool, Body(default=False)]
    code: Annotated[str, Body(min_length=8, max_length=12)]
    reference: Annotated[str | None, Body(default=None)]
    topic: Annotated[str | None, Body(default=None)]
    subject: Annotated[str | None, Body(default=None)]
    description: Annotated[str | None, Body(default=None)]
    deadline: Annotated[datetime, Body(default=None)]
    status: Annotated[str, Body()]
    owner: Annotated[str | None, Body(default=None)]


class UpdateTask(BaseModel):
    updatedAt: Annotated[datetime, Body(default=datetime.now())]
    active: Annotated[bool, Body(default=False)]
    reference: Annotated[str | None, Body(default=None)]
    topic: Annotated[str | None, Body(default=None)]
    subject: Annotated[str | None, Body(default=None)]
    description: Annotated[str | None, Body(default=None)]
    deadline: Annotated[datetime, Body(default=None)]
    status: Annotated[str, Body(default=None)]
    owner: Annotated[str | None, Body(default=None)]


class RemoveTask(BaseModel):
    deletedAt: Annotated[datetime, Body(default=datetime.now())]
    active: Annotated[bool, Body(default=False)]
    softDeleted: Annotated[bool, Body(default=True)]
