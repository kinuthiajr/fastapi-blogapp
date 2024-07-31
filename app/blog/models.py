# Contains database model for the blog service

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .database import Base

class Blog(Base):

    __tablename__ = 'blog'

    id = Column(UUID(as_uuid=True), primary_key = True, default=uuid.uuid4)
    title = Column(String,nullable=False)
    content = Column(String,nullable=True)
    rating = Column(Integer, default=0)
    seen = Column(Integer, default=0)

    def __repr__(self):
        return f"<Blog(id={self.id}, title={self.title})>"

