from pydantic import BaseModel


class MovieSchema(BaseModel):
    id: int
    title: str
    genre: str
    user_id: int
    
    
class CreateMovieSchema(BaseModel):
    title: str
    genre: str