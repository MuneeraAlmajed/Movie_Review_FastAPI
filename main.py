from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
# models
from models.user import UserModel
from models.movie import MovieModel
from models.review import ReviewModel

# Controllers
from controllers.users import router as UsersRouter
from controllers.movies import router as MovieRouter
from controllers.reviews import router as ReviewRouter


app = FastAPI()

app.include_router(UsersRouter, prefix='/api')
app.include_router(MovieRouter, prefix='/api')
app.include_router(ReviewRouter, prefix='/api')


@app.get('/health')
def health_check():
  return {'message': 'Api is running'}


