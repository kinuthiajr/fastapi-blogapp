# Contains pydantic models for validation and serialization

from pydantic import BaseModel,UUID4

class BlogBase(BaseModel):
    """"
    Base for other blog-related models and common attributes
    """
    title:str
    content: str
    rating: int=0
    seen: int=0

class BlogCreate(BlogBase):
    """
    Inherits from BlogBase class to create a blog
    """
    pass

class Blog(BlogBase):
    id: UUID4

    class Config:
        orm_mode = True