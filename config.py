import os

basedir = os.path.abspath(os.path.dirname(__file__))
CSRF_ENABLED = True
SECRET_KEY = 'hard to guess string'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@ip/db'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_COMMIT_ON_TEARDOWN=True
SQLALCHEMY_TRACK_MODIFICATIONS=True
FLASKY_ADMIN='admin'
FLASKY_FORBID='xulu'