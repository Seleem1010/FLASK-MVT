import os
class Config:
    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI= "sqlite:///db.sqlite"
    # MEDIA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "media")
    # MEDIA_URL = "/media/"


class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI= "postgresql://postgres:Mo#Selim@localhost:5432/posts"
    # MEDIA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "media")
    # MEDIA_URL = "/media/"

project_config= {
    "dev": DevelopmentConfig,
    "prd":ProductionConfig
}