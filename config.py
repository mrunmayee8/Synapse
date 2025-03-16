import os

class Config:
    # Secret key for session security (modify this)
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key_here")

    # PostgreSQL Database Configuration (Modify with your credentials)
    DB_USERNAME = os.getenv("DB_USERNAME", "your_username")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "your_password")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "allergen_db")

    # Construct Database URL
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable event system to save memory

    # File Upload Settings
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size