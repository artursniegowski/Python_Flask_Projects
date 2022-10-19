# env variables !
from dotenv import load_dotenv
load_dotenv()
import os

################################################################################
## sensitive data ###
#####################
# In order to generate the csrf token, you must have a secret key, this is 
# usually the same as your Flask app secret key. If you want to use another 
# secret key, config it.
# env variables ! - dont change here !
FLASK_SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
# user defined email and app password - has to be GMAIL !
# env variables ! - dont change here !
MY_EMAIL = os.environ.get('MY_EMAIL')
GMAIL_APP_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')
# email adress where we want to send the notification to
HOST_EMAIL_FOR_CONTACT_FORM = os.environ.get("HOST_EMAIL_FOR_CONTACT_FORM")
# PostgreSQL database - Database url configured in HEROKU from resources tab!
# app config will use "DATABASE_URL" environment variable if provided, but if it's None 
# (e.g. when running locally) then we can provide sqlite:///blog.db as the alternative.
# this variable DATABASE_URL is defined only on Heroku !!! in the Config Vars after adding the 
# Heroku PostgreSQL Database from resources

# The URI should start with postgresql:// instead of postgres://. 
# SQLAlchemy used to accept both, but has removed support for the postgres name.
# for the DATABASE_URL
POSTGRESQL_DATABASE_URL = os.environ.get("DATABASE_URL", 'sqlite:///blog.db')
if 'postgres://' in POSTGRESQL_DATABASE_URL:
    POSTGRESQL_DATABASE_URL = POSTGRESQL_DATABASE_URL.replace('postgres://', 'postgresql://')
################################################################################