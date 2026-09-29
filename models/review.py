from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel


class ReviewModel(BaseModel):

    __tablename__ = "reviews"

    content = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    movie = relationship("MovieModel", back_populates="reviews")
    user = relationship("UserModel", back_populates="reviews")
    