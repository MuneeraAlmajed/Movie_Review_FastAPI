from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel

class MovieModel(BaseModel):
    __tablename__ = 'movies'
    
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('UserModel', back_populates='movies')
    reviews = relationship('ReviewModel', back_populates='movie')