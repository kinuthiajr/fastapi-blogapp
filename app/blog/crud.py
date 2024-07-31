# Contains the create, retrieve, update, delete operations

from sqlalchemy.orm import Session
from .import models, schemas
from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel,UUID4

def create_blog(db:Session,blog:schemas.BlogCreate):
    db_blog = models.Blog(**blog.dict())
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def get_blog(db:Session, blog_id:UUID4):
    
    """
     retrieve a individual blog
    """
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()

def get_all_blogs(db:Session, skip: int=0,limit: int=10):
    """"
    retrieve all blogs with pagination of 10
    """
    return db.query(models.Blog).offset(skip).limit(limit).all()

def update_blog(db:Session, blog_id:UUID4, blog:schemas.BlogCreate):
    """"
    edit an individual blog
    """
    db_blog = db.query(models.Blog).filter(models.Blog.id==blog_id).first() #find a blog by id
    if db_blog:
        db_blog.title = blog.title
        db_blog.content = blog.content
        db_blog.rating = blog.rating
        db_blog.seen = blog.seen
        db.commit()
        db.refresh(db_blog)
    return db_blog

def delete_blog(db:Session, blog_id:UUID4):
    """
    Erase/ remove an individual blog
    """
    db_blog = db.query(models.Blog).filter(models.Blog.id==blog_id).first()
    if db_blog:
        db.delete(db_blog)
        db.commit()
    return db_blog