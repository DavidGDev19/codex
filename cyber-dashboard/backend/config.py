"""Application configuration classes."""

import os


class Config:
    """Base configuration."""

    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost")
    RBAC_ROLES = ["admin", "user"]  # TODO: expand roles


class DevConfig(Config):
    """Development settings."""

    DEBUG = True


class ProdConfig(Config):
    """Production settings."""

    DEBUG = False
