from typing import List
from bson import ObjectId
from fastapi import APIRouter, Body, HTTPException, status
from pymongo import ReturnDocument
from orders.schemas import one, many
from orders.models import Order, CreateOrder, UpdateOrder, RemoveOrder
from database.mongodb import orders

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model_by_alias=False, response_model=Order)
async def create(inputs: CreateOrder = Body(...)):
    data = await orders.insert_one(inputs.model_dump(by_alias=True, exclude=["id"]))
    created = await orders.find_one({"_id": data.inserted_id})
    return created


@router.get("/", response_model_by_alias=False, response_model=List[Order])
async def find_many():
    data = await orders.find(limit=100)
    return many(data)


@router.get("/{id}", response_model_by_alias=False, response_model=Order)
async def find_one(id: str):
    if (data := await orders.find_one({"_id": ObjectId(id)})) is not None:
        return one(data)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found!")


@router.patch("/{id}", response_model_by_alias=False)
async def update(id: str, inputs: UpdateOrder = Body(...)):
    if (data := await orders.find_one({"_id": ObjectId(id)})) is None:
        return data

    inputs = {
        key: value for key, value in inputs.model_dump(by_alias=True).items() if value is not None
    }
    if len(inputs) >= 1:
        data = await orders.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(inputs)},
                                                return_document=ReturnDocument.AFTER)

        if data is not None:
            return f"Data has been updated!"
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found!")

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found!")


@router.delete("/{id}")
async def remove(id: str, inputs: RemoveOrder = Body(...)):
    if (data := await orders.find_one({"_id": ObjectId(id)})) is None:
        return data

    inputs = {
        key: value for key, value in inputs.model_dump(by_alias=True).items() if value is not None
    }

    if data is not None:
        if inputs["softDeleted"]:
            data = await orders.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(inputs)},
                                                    return_document=ReturnDocument.AFTER)
            if data is not None:
                return f"Data has been removed!"
        else:
            data = await orders.delete_one({"_id": ObjectId(id)})
            if data.deleted_count == 1:
                return f"Data has been permanently removed!"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found!")
