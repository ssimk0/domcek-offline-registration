"""Application configuration."""
import os


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('CONDUIT_SECRET', 'secret-key')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    JWT_HEADER_TYPE = 'Token'


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    CACHE_TYPE = 'simple'


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
