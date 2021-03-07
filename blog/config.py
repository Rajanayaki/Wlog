import os

class Config:
    SECRET_KEY = 'be0064082585eb77bcbbfb4da259bd78'
    SQLALCHEMY_DATABASE_URI= 'sqlite:///site.db'
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USERNAME="noreplydemo20@gmail.com"
    MAIL_PASSWORD="Happiebird@20"
