import base64
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import url_for
db= SQLAlchemy()


#database post model
class Category(db.Model):
    __tablename__= 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    
    def __str__(self):
        return self.name

#database post model
class Post(db.Model):
    __tablename__= 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    body = db.Column(db.String,nullable=False)
    image = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    category_id = db.Column(db.Integer,db.ForeignKey("categories.id"))

    def __str__(self):
        return self.title
    
    

    def delete_post(self):
        db.session.delete(self)
        db.session.commit()
        return True

    @classmethod
    def get_specific_object(cls, id):
        return  cls.query.get_or_404(id)
    
    @property
    def get_view_url(self):
        return url_for("MVT.posts_view", id=self.id)

    @property
    def get_delete_url(self):
        return url_for("MVT.posts_delete", id=self.id)