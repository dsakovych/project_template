import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, orm
from app.settings import project_config

####################################################################################################
####################################################################################################


def create_db(app):
    db = SQLAlchemy()
    db.init_app(app)

    db_engine_ = create_engine(project_config.SQLALCHEMY_DATABASE_URI)

    session_ = orm.sessionmaker(bind=db_engine_)

    return db_engine_, session_

####################################################################################################
####################################################################################################


def create_app(config=project_config):
    app = Flask(__name__)
    app.config.from_object(config)

    if not os.path.exists(os.path.join(app.config['APP_DIR'], 'var', 'log')):
        os.makedirs(os.path.join(app.config['APP_DIR'], 'var', 'log'))

    handlers = [
        logging.FileHandler(
            os.path.join(project_config.APP_DIR, 'var', 'log', 'syslog.log')
        ),
        logging.StreamHandler()
    ]

    logging.basicConfig(level=logging.INFO,
                        format=project_config.LOGGING_FORMATTER,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=handlers)

    return app

####################################################################################################
####################################################################################################


app = create_app()

db_engine, session = create_db(app)


from app import views

logging.warning(f'Running app with *{project_config.CONFIG_NAME}* config')
