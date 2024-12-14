from pydantic import BaseModel
class UserCreate(BaseModel):
    username: str
    password: str
class BlogCreate(BaseModel):
    title: str
    content: str