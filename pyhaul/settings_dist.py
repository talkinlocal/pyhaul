# -*- coding: utf-8 -*-
import os


class Config(object):
    SECRET_KEY = 'change me'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    LOG_FILE = 'pyhaul.log'
    ALLIANCE_ID = 0 # Put your alliance ID; see EVE API or use zkillboard
    AUTH = {
        "domain": "example.com", # Auth website domain
        "alliance": "Alliance Name", # Alliance full name 
        "allianceshort": "ALLN" # Alliance ticker
    }
    SESSION_COOKIE_NAME = 'pyhaul_'
    EVE = {
        'ALLIANCE_KEY_ID': 0, # API Key ID # for Exec CEO Corp key
        'ALLIANCE_KEY_VCODE': '' # vCode for the same
    }
    USER_GROUPS  = ('logistics',)  # Tuple of groups allowed to use this tool
    ADMIN_GROUPS = ('admin','admin-logistics')  # Tuple of groups to allow super admin.


class ProdConfig(Config):
    CACHE_TYPE = 'simple'
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:pass@dbhost/dbname'  # DB URL
    REDIS = '127.0.0.1'
    #LDAP = {
    #    "server": "ldap:///ldap.local/",
    #    "admin": "cn=secret,dc=example,dc=com",
    #    "password": "--secret--",
    #    "basedn": "dc=example,dc=com",
    #    "memberdn": "ou=People,dc=example,dc=com"
    #}
    APPLICATION_ROOT = '/pyhaul/'
    REDIS_URL = "redis://:password@localhost:6379/0"


class DevConfig(Config):
    CACHE_TYPE = 'simple'
    DEBUG = True
    DB_NAME = 'pyhaul.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    SQLALCHEMY_ECHO = True
    REDIS = '127.0.0.1'
    #LDAP = {
    #    "server": "ldap:///127.0.0.1/",
    #    "admin": "cn=admin,dc=example,dc=local",
    #    "password": "admin",
    #    "basedn": "dc=example,dc=local",
    #    "memberdn": "ou=People,dc=example,dc=local"
    #}
    REDIS_URL = "redis://:password@localhost:6379/0"
