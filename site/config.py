import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # used by flask to init crypto, flask-wtf uses to protect against CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'guess'
    
    #setup sqlalchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    #DB_USER = os.environ.get('DB_USER') or 'testuser'
    #DB_PASS = os.environ.get('DB_PASS') or '123'
    #DB_PROJ = os.environ.get('DB_PROJ') or 'assign_3'
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://' + DB_USER + ':' + DB_PASS + '@localhost:3306/' + DB_PROJ
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #setup app tools
    SPELLCHECK_TEMP_DIR = os.environ.get('SPELLCHECK_TEMPDIR') or os.path.join(basedir, 'temp')
    SPELLCHECK_BIN_DIR = os.environ.get('SPELLCHECK_BINDIR') or os.path.join(basedir, 'bin')
    SPELLCHECK_TOOL = os.environ.get('SPELLCHECK_TOOL') or os.path.join(SPELLCHECK_BIN_DIR, 'a.out')
    SPELLCHECK_WORDLIST = os.environ.get('SPELLCHECK_WORDLIST') or os.path.join(SPELLCHECK_BIN_DIR, 'wordlist.txt')
    
    SPELLCHECK_ADMIN_PW = os.environ.get('SPELLCHECK_ADMIN_PW') or 'Administrator@1'
    SPELLCHECK_ADMIN_MFA = os.environ.get('SPELLCHECK_ADMIN_MFA') or '12345678901'



