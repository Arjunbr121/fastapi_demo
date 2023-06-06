from passlib.context import CryptContext


pwd_context = CryptContext(schemes= ["bcrypt"],deprecated = "auto")

def hash(pasword: set):
    return pwd_context.hash(pasword) 

def verify(plain_pasword,hashed_pasword):
    return pwd_context.verify(plain_pasword,hashed_pasword)