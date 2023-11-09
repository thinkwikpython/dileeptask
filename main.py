# main.py
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from models import Base, Blog, Comment
from database import SessionLocal, get_db
from sqlalchemy.orm import Session

app = FastAPI()

# Endpoint to add a blog
@app.post("/blogs/")
def create_blog(title: str, body: str):
    db = SessionLocal()
    blog = Blog(title=title, body=body)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    db.close()
    return blog

# Endpoint to get a blog by ID
@app.get("/blogs/{blog_id}")
def read_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")

    return {"blog_id":blog.id, "title":blog.title, "body":blog.body}

# Endpoint to get all blogs
@app.get("/blogs")
def read_blogs(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs

# Endpoint to add a comment to a blog
@app.post("/blogs/{blog_id}/comment/")
def create_comment(blog_id: int, comment: str):
    db = SessionLocal()
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    comment = Comment(comment=comment, blog_id=blog_id)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    db.close()
    return comment

# Endpoint to get all comments for a blog
@app.get("/blogs/{blog_id}/comments/")
def get_blog_comments(blog_id: int):
    db = SessionLocal()
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    comments = blog.comments
    db.close()
    return comments
