from sqlalchemy.orm import sessionmaker, Session
from models.user import UserModel
from models.movie import MovieModel
from models.review import ReviewModel

from data.user_data import user_list
from data.movie_data import movie_list, review_list
from config.environment import DATABASE_URL
from sqlalchemy import create_engine
from models.base import Base


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

try:
    print("Recreating database...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    print("seeding the database...")
    db = SessionLocal()

    db.add_all(user_list)
    db.commit()
    
    db.add_all(movie_list)
    db.commit()
    
    db.add_all(review_list)
    db.commit()

    db.close()

    print("Database seeding complete! 👋")
except Exception as e:
    print("An error occurred:", e)