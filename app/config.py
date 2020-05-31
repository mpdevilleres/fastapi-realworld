from pathlib import Path

BASE_DIR = str(Path(__file__).resolve().parent.parent)

SQLALCHEMY_DATABASE_URL = f"sqlite:///{BASE_DIR}/app.db"
