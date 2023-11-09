# models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    comments = relationship("Comment", back_populates="blog")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)  # Make sure this line is present
    blog_id = Column(Integer, ForeignKey("blogs.id"))

    blog = relationship("Blog", back_populates="comments")
