import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, orm
from app.settings import project_config
from app.utils.elk_utils.logstash import TCPLogstashHandler

####################################################################################################
####################################################################################################


def create_db(app):
    db = SQLAlchemy()
    db.init_app(app)

    db_engine_ = create_engine(project_config.SQLALCHEMY_DATABASE_URI)

    session_ = orm.sessionmaker(bind=db_engine_)
    session_ = session_()

    return db_engine_, session_

####################################################################################################
####################################################################################################


def create_app(config=project_config):
    app_ = Flask(__name__)
    app_.config.from_object(config)

    if not os.path.exists(os.path.join(app_.config['APP_DIR'], 'var', 'log')):
        os.makedirs(os.path.join(app_.config['APP_DIR'], 'var', 'log'))

    handlers = [
        logging.FileHandler(
            os.path.join(project_config.APP_DIR, 'var', 'log', 'syslog.log')
        ),
        logging.StreamHandler(),
        TCPLogstashHandler(host=project_config.LOGSTASH_HOST, port=project_config.LOGSTASH_PORT),
    ]

    logging.basicConfig(level=logging.INFO,
                        format=project_config.LOGGING_FORMATTER,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=handlers)

    return app_

####################################################################################################
####################################################################################################


app = create_app()

db_engine, session = create_db(app)


from app import views, models

logging.warning(f'Running app with *{project_config.CONFIG_NAME}* config')
