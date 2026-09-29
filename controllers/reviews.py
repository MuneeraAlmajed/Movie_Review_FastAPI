from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.review import ReviewModel
from serializers.review import ReviewSchema, CreateReviewSchema
from database import get_db
from dependencies.get_current_user import get_current_user

router = APIRouter()


@router.get("/reviews", response_model=list[ReviewSchema])
def get_reviews(db: Session = Depends(get_db)):
    return db.query(ReviewModel).all()


@router.post("/reviews", response_model=ReviewSchema, status_code=201)
def create_review(
    review: CreateReviewSchema,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    new_review = ReviewModel(
        content=review.content,
        rating=review.rating,
        movie_id=review.movie_id,
        user_id=user.id
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review



@router.put("/reviews/{review_id}", response_model=ReviewSchema)
def update_review(
    review_id: int,
    review: CreateReviewSchema,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    existing_review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()

    if not existing_review:
        raise HTTPException(status_code=404, detail="Review not found")

    if existing_review.user_id != user.id:
        raise HTTPException(status_code=403, detail="You can only update your own reviews")

    existing_review.content = review.content
    existing_review.rating = review.rating
    existing_review.movie_id = review.movie_id

    db.commit()
    db.refresh(existing_review)

    return existing_review

@router.delete("/reviews/{review_id}")
def delete_review(
    review_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    existing_review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()

    if not existing_review:
        raise HTTPException(status_code=404, detail="Review not found")

    if existing_review.user_id != user.id:
        raise HTTPException(status_code=403, detail="You can only delete your own reviews")

    db.delete(existing_review)
    db.commit()

    return {"message": "Review deleted successfully"}