import os


class Config:
    '''
    General configuration parent class
    '''

    QUOTES_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    QUOTES_API_KEY = os.environ.get('QUOTES_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/watchlist'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True