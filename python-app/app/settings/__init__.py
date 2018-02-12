import os

from .common import (DevelopmentConfig, TestingConfig, ProductionConfig)

from .ml_config import Config

config = {
    'develop': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

project_config = config[os.getenv('PYTHON_APP_CONFIG', 'develop')]
ml_config = Config
