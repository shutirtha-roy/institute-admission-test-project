from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from server.models.product_review import ProductReview, UpdateProductReview


router = APIRouter()

@router.post("/", response_description="Review added to the database")
async def add_product_review(review: ProductReview) -> dict:
    await review.create()
    return {"message": "Review added successfully"}