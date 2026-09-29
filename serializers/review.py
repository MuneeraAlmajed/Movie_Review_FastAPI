from pydantic import BaseModel


class ReviewSchema(BaseModel):
    id: int
    content: str
    rating: int
    movie_id: int
    
    
class CreateReviewSchema(BaseModel):
    content: str
    rating: int
    movie_id: int
    