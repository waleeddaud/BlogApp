from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship



# Models
class Blog(Base):
    __tablename__ = "Blog"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('User.id'))
    author = relationship("User", back_populates="blogs")



class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    blogs = relationship("Blog", back_populates="author")