from .database import Base
from sqlalchemy import TIMESTAMP, Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__="posts"

    id = Column(Integer,primary_key=True,nullable=False)
    title =Column(String,nullable=False)
    content=Column(String,nullable=False)
    published=Column(Boolean,server_default='TRUE',nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id = Column(Integer,ForeignKey ("login.id",ondelete = "CASCADE"),nullable = False)
    owner = relationship("Login")

class Login(Base):
    __tablename__="login"
    id = Column(Integer,primary_key=True,nullable=False)
    Username = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True)
    pasword = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    phone_number = Column(String)

class Vote(Base):
    __tablename__ = "votes"
    user_id=Column(Integer,ForeignKey("login.id",ondelete="CASCADE"),primary_key=True)
    post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
