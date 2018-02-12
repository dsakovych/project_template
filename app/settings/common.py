import os


class Config:
    CONFIG_NAME = 'default'

    HOST = '127.0.0.1'
    PORT = 5000

    APP_DIR = os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )

    LOGGING_FORMATTER = '[%(asctime)s] - %(levelname)s - %(message)s'

    # DB settings
    DB_USER = 'root'
    DB_PASS = 'root'
    DB_HOST = 'localhost'
    DB_PORT = 3306  # MySQL
    DB_NAME = 'test_db'

    # sqlalchemy settings
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class ProductionConfig(Config):
    CONFIG_NAME = 'production'


class DevelopmentConfig(Config):
    CONFIG_NAME = 'develop'


class TestingConfig(Config):
    CONFIG_NAME = 'testing'
