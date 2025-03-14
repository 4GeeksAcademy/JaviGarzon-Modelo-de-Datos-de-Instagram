from flask_sqlalchemy import SQLAlchemy, ForeingKey
from sqlalchemy import String, Integer, SQLAlchemy
from sqlalchemy.orm import Column


db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    firstname = Column(String(50), nullable=False)
    secondname = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)

def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
             "firstname": self.firstname,
             "email": self.email,
        }

class Comment(db.Model):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(200), nullable=False)
    author_id = Column(Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = Column()

    def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "author": self.author_id, 
             "post": self.post_id, 
        }

comments = relationship('comment', backref='user', lazy=True)