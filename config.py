import os


BASE_DIR = os.path.abspath(
    os.path.dirname(__file__)
)


class Config:

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "benefitshield-secret-key"
    )

    DATABASE_PATH = os.path.join(
        BASE_DIR,
        "database",
        "database.db"
    )

    UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        "static",
        "uploads"
    )

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    ALLOWED_EXTENSIONS = {
        "pdf",
        "png",
        "jpg",
        "jpeg",
        "webp"
    }