import os

basedir = os.path.abspath(os.path.dirname(__file__))
savedir = os.path.join(basedir, 'saved')

SECRET_KEY = 'development key'
CSRF_ENABLED = True
DEBUG = True

#==============================================================================
# Database
#==============================================================================

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
