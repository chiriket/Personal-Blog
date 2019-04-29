import os


class Config:
    '''
    General configuration parent class
    '''

    # QUOTES_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    # QUOTES_API_KEY = os.environ.get('QUOTES_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://shirley:1234@localhost/personalblog'
    # SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST = 'app/static/photos'


     # Sending Emails
    MAIL_SERVER=os.environ.get('MAIL_SERVER')
    MAIL_PORT=os.environ.get('MAIL_PORT')
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')

    @staticmethod
    def init_app(app):
        pass


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

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://shirley:1234@localhost/personalblog'

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    # 'test':TestCo
}