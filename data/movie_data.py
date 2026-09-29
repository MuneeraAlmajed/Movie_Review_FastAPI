from models.movie import MovieModel
from models.review import ReviewModel

movie_list = [
    MovieModel(title="Inception", genre="Sci-Fi", user_id=1),
    MovieModel(title="Titanic", genre="Romance", user_id=1),
    MovieModel(title="The Dark Knight", genre="Action", user_id=2),
]

review_list = [
    ReviewModel(content="Amazing movie", rating=5, movie_id=1),
    ReviewModel(content="Very good", rating=4, movie_id=1),
    ReviewModel(content="Great story", rating=5, movie_id=2),
]