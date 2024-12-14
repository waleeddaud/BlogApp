from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Optional
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from database import  get_db
from models import User, Blog
from schemas import UserCreate , BlogCreate
from utils import get_hashed_password, verify_password, create_access_token
from deps import get_current_user


# Define constants
SECRET_KEY = "2ba3594354d4eb2251b0312ed878273f67d8760acdd9319731ccc4647ae623e2"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30









# # OAuth2 token bearer setup
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
# def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise HTTPException(status_code=401, detail="Invalid token")
#         user = db.query(User).filter(User.username == username).first()
#         if user is None:
#             raise HTTPException(status_code=401, detail="User not found")
#         return user
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Could not validate credentials")

# FastAPI instance
app = FastAPI()

# Routes
@app.post("/signup/")
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    find_user = db.query(User).filter(User.username == user.username).first()
    if find_user:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_password = get_hashed_password(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"username": new_user.username}

@app.post("/login/")
async def login_for_access_token(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form.username).first()
    if user is None or not verify_password(form.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(subject=user.username)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/me")
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.post("/me/blog/")
async def create_blog(blog: BlogCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    new_blog = Blog(title=blog.title, content=blog.content, user_id=current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {"message": "Blog created successfully", "blog": new_blog}

@app.get("/me/blog/")
async def get_blog_by_title(title: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    blog = db.query(Blog).filter(Blog.title == title).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"Blog": blog}

@app.put("/me/blog/")
async def update_blog(blog: BlogCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    existing_blog = db.query(Blog).filter(Blog.title == blog.title).first()
    if not existing_blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    existing_blog.content = blog.content
    db.commit()
    db.refresh(existing_blog)
    return {"message": "Blog updated successfully", "blog": existing_blog}

@app.delete("/me/blog/")
async def delete_blog(title: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    blog_to_delete = db.query(Blog).filter(Blog.title == title).first()
    if not blog_to_delete:
        raise HTTPException(status_code=404, detail="Blog not found")
    db.delete(blog_to_delete)
    db.commit()
    return {"message": f"Blog with title '{title}' deleted"}