from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

def add(item):
    db.session.add(item)

def save_all():
    db.session.commit()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(64), nullable = False)
    notes = db.Column(db.Text, default = '', nullable = False)
    done = db.Column(db.Boolean, default=False, nullable = False) 
    created_at = db.Column(db.DateTime, nullable = False) 
    completed_at = db.Column(db.DateTime, default=None, nullable = True) 

    def __init__(self, title, notes=''):
        self.title = title
        self.notes = notes
        self.created_at = datetime.datetime.utcnow()

    def __repr__(self):
        status = "Completed" if self.done else "Not Complete"
        return "<Task %d:%s %s.>"%(self.id or -1, self.title, status)

    def __str__(self):
        return self.__repr__().replace("<", "").replace(">", "")

    def complete(self):
        self.done = True
        self.completed_at = datetime.datetime.utcnow()
