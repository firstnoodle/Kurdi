import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'kurdi.db'
USERNAME = 'admin'
PASSWORD = 'nazanim'

# Cross Site Request Forgery
WTF_CSRF_ENABLED = True

# use random key generator https://github.com/rjw57/hdcp-genkey
SECRET_KEY = 'my_precious'

#define the full path for the DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)
