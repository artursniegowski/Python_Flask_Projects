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
################################################################################