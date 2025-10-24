import os

class Config:
    SECRET_KEY = 'admin2201'
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://postgres:admin2201@localhost:5432/ecom'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
