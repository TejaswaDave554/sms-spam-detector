import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32)
    MAX_CONTENT_LENGTH = 16 * 1024
    MODEL_PATH = os.environ.get('MODEL_PATH', 'models/spam-sms-mnb-model.pkl')
    CV_PATH = os.environ.get('CV_PATH', 'models/cv-transform.pkl')

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    DEBUG = True
    TESTING = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
