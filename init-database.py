"""
Database Initialization Script
For quickly migrating into a new environment
"""

from project import db, model

# Creating Table Structure
# May fail if there are existing tables
model.initialize()
db.create_all()
