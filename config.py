import os


class Config:

    QUOTES_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    QUOTES_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/watchlist'