from .. import db


class User(db.Model):
    # Table Name
    __tablename__ = 'user'

    # Table Columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.VARCHAR(32), nullable=False, unique=True)

    # Table Relationships
    #  - (you don't have to have some)

    # Record Constructing
    def __init__(self, name: str):
        self.name = name

    # Record Representing
    def __repr__(self):
        return f'<User#{self.id}:{self.name}>'
