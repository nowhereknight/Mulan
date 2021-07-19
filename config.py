import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://admin:12QwAsZx@flask-database.cekr24jx0ek8.us-east-1.rds.amazonaws.com:3306/flask_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENTERPRISES_PER_PAGE = 3
