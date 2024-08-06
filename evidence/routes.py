from typing import List
from bson import ObjectId
from fastapi import APIRouter, Body, HTTPException, status
from pymongo import ReturnDocument
from evidence.schemas import one, many
from evidence.models import Evidence, CreateEvidence, UpdateEvidence, RemoveEvidence
from database.mongodb import evidence

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model_by_alias=False, response_model=Evidence)
async def create(inputs: CreateEvidence = Body(...)):
    data = await evidence.insert_one(inputs.model_dump(by_alias=True, exclude=["id"]))
    created = await evidence.find_one({"_id": data.inserted_id})
    return created


@router.get("/", response_model_by_alias=False, response_model=List[Evidence])
async def find_many():
    data = await evidence.find(limit=100)
    return many(data)


@router.get("/{id}", response_model_by_alias=False, response_model=Evidence)
async def find_one(id: str):
    if (data := await evidence.find_one({"_id": ObjectId(id)})) is not None:
        return one(data)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found!")


@router.patch("/{id}", response_model_by_alias=False)
async def update(id: str, inputs: UpdateEvidence = Body(...)):
    if (data := await evidence.find_one({"_id": ObjectId(id)})) is None:
        return data

    inputs = {
        key: value for key, value in inputs.model_dump(by_alias=True).items() if value is not None
    }
    if len(inputs) >= 1:
        data = await evidence.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(inputs)},
                                                  return_document=ReturnDocument.AFTER)

        if data is not None:
            return f"Data has been updated!"
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found!")

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found!")


@router.delete("/{id}")
async def remove(id: str, inputs: RemoveEvidence = Body(...)):
    if (data := await evidence.find_one({"_id": ObjectId(id)})) is None:
        return data

    inputs = {
        key: value for key, value in inputs.model_dump(by_alias=True).items() if value is not None
    }

    if data is not None:
        if inputs["softDeleted"]:
            data = await evidence.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(inputs)},
                                                      return_document=ReturnDocument.AFTER)
            if data is not None:
                return f"Data has been removed!"
        else:
            permanently = await evidence.delete_one({"_id": ObjectId(id)})
            if permanently.deleted_count == 1:
                return f"Data has been permanently removed!"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found!")
