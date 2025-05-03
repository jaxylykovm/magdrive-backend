import os

DB_USER = os.getenv("DB_USER", "magzhanjaxylykov")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")  # если пароль не задан
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "magdrive")

SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
