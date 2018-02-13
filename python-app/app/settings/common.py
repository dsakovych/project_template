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
    DB_HOST = '127.0.0.1'
    DB_PORT = 3306  # MySQL
    DB_NAME = 'test_db'

    # sqlalchemy settings
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # ELK settings
    LOGSTASH_HOST = '127.0.0.1'
    LOGSTASH_PORT = 5044


class DockerConfig(Config):
    CONFIG_NAME = 'docker'

    HOST = '0.0.0.0'

    # DB settings
    DB_USER = 'root'
    DB_PASS = 'root'
    DB_HOST = '0.0.0.0'
    DB_PORT = 3306  # MySQL
    DB_NAME = 'test_db'
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    LOGSTASH_HOST = '0.0.0.0'


class DevelopmentConfig(Config):
    CONFIG_NAME = 'develop'


class ProductionConfig(Config):
    CONFIG_NAME = 'production'
