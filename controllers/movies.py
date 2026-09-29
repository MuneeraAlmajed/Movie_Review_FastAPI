from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.movie import MovieModel
from serializers.movie import MovieSchema, CreateMovieSchema
from database import get_db
from dependencies.get_current_user import get_current_user

router = APIRouter()

