from typing import Optional
from pydantic import BaseModel, EmailStr, conint,fields
from datetime import datetime 

class BasePost(BaseModel):
    title:str
    content:str
    published:bool=True

    class Config:
        orm_mode =True

    
class CreatePost(BasePost):
    pass

class LoginPost(BaseModel):
    Username:str
    email:EmailStr
    pasword:str
    

class Loginval(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
        
    class Config:
        orm_mode =True

# class Post1(Loginval):
#     owner_id: int
#     owner:Loginval
    
#     class Config:
#         orm_mode=True

class Userlogin(BaseModel):
    username:str
    email:EmailStr
    owmner:str
    pasword:str

class UserVal(BaseModel):
    username:str
    email:EmailStr
    pasword: str

class Post(BasePost):
    id :int
    created_at:datetime
    owner_id: int
    owner: Loginval

    class Config:
        orm_mode =True

class Postout(BaseModel):
    Post:Post
    Votes:int

    class Config:
        orm_mode =True

class Userlogin(BaseModel):
    username:str
    email:EmailStr
    # pasword:str

class Token(BaseModel):
    acess_token: str
    token_type : str

class Tokendata(BaseModel):
    id:Optional[str]=None

class GwtPostid(BaseModel):
    title:str
    content:str
    id:int
    created_at:datetime
    # owner_id:int
    
    class Config:
        orm_mode =True

class Vote(BaseModel):
    post_id :int
    dir :conint(le=1)

    
