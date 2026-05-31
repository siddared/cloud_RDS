SECRET_KEY = "cloud_rds_secret_key"

DB_USER = "admin"

DB_PASSWORD ="admin12345"

DB_HOST = "database-1.ctuk4si20nie.ap-south-1.rds.amazonaws.com"

DB_NAME = "cloudrds"

SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False