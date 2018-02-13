import os

from .common import (DevelopmentConfig, DockerConfig, ProductionConfig)

from .ml_config import Config

config = {
    'develop': DevelopmentConfig,
    'docker': DockerConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

project_config = config[os.getenv('PYTHON_APP_CONFIG', 'docker')]
ml_config = Config
