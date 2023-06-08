class Config:
    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI= "sqlite:///db.sqlite"


class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI= "postgresql://postgres:Mo#Selim@localhost:5432/posts"


project_config= {
    "dev": DevelopmentConfig,
    "prd":ProductionConfig
}