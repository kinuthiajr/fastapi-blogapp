from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import create_blog, get_all_blogs,get_blog,delete_blog,update_blog
from ..schemas import BlogCreate,Blog
from ..database import get_db
from sqlalchemy.dialects.postgresql import UUID
from pydantic import UUID4
from typing import List

router = APIRouter(
    prefix="/blogs",
    tags = ["blogs"],
    responses={404:{"description":"Not Found"}}
)

@router.post("/",response_model=Blog)
async def create_blog_route(blog:BlogCreate,db:Session=Depends(get_db)):
    return create_blog(db=db,blog=blog)

@router.get("/{blog_id}")
async def read_a_blog_route(blog_id:UUID4, db:Session = Depends(get_db)):
    db_blog = get_blog(db=db,blog_id=blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404,details="Blog not found")
    return db_blog

@router.get("/",response_model=List[Blog])
async def read_blogs_route(db:Session=Depends(get_db),skip:int=0, limit:int=10):
    db_blogs = get_all_blogs(db=db,skip=skip,limit=limit)
    if db_blogs is None:
        raise HTTPException(status_code=404, details="No blogs created yet")
    return db_blogs

@router.put("/{blog_id}",response_model=Blog)
async def update_blog_route(blog_id:UUID4,blog:BlogCreate, db:Session=Depends(get_db)):
    db_blog = update_blog(blog_id=blog_id,db=db)
    if not db_blog:
        raise HTTPException(status_code=404, details="Blog not found")
    return update_blog(blog_id=blog_id,db=db,blog=blog)

@router.delete("/{blog_id}",response_model=Blog)
async def delete_blog_route(blog_id:UUID4, db:Session=Depends(get_db)):
    db_blog = delete_blog(blog_id=blog_id,db=db)
    if db_blog is None:
        raise HTTPException(status_code=404,details="Can not delete blog")
    return db_blog
