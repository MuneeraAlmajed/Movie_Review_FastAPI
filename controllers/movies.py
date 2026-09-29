from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.movie import MovieModel
from serializers.movie import MovieSchema, CreateMovieSchema
from database import get_db
from dependencies.get_current_user import get_current_user

router = APIRouter()

@router.get('/movies', response_model=list[MovieSchema])
def get_movies(db: Session = Depends(get_db)):
    return db.query(MovieModel).all()

@router.post('/movies',response_model=MovieSchema, status_code=201)
def create_movie(
    movie: CreateMovieSchema,
    db: Session = Depends(get_db),
    user= Depends(get_current_user)
):
    new_movie=MovieModel(
        title=movie.title,
        genre=movie.genre,
        user_id=user.id
    )
    
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    
    return new_movie

@router.put('/movies/{movie_id}',response_model=MovieSchema)
def update_movie(
    movie_id: int,
    movie: CreateMovieSchema,
    db: Session = Depends(get_db),
    user= Depends(get_current_user)
    
):
    existing_movie = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    
    if not existing_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    existing_movie.title = movie.title
    existing_movie.genre = movie.genre

    db.commit()
    db.refresh(existing_movie)

    return existing_movie


@router.delete("/movies/{movie_id}")
def delete_movie(
    movie_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    existing_movie = db.query(MovieModel).filter(MovieModel.id == movie_id).first()

    if not existing_movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    db.delete(existing_movie)
    db.commit()

    return {"message": "Movie deleted successfully"}
    