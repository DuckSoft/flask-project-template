"""
Project Configurations for Flask Application
"""

# Development
DEBUG = True
LISTEN_HOST_DEV = r'127.0.0.1'
LISTEN_PORT_DEV = 5000

# Production
LISTEN_HOST_PRODUCTION = r'0.0.0.0'
LISTEN_PORT_PRODUCTION = 8080

# Session
SECRET_KEY = r'xsa2Df323rUF9*EWFH&*h(dsa#Y(#&HDWDH(/,?RT'

# SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = r"mysql://root:rootpassword@localhost:3306/database?charset=utf8mb4"
