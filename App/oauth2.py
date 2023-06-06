from datetime import timedelta,datetime
from fastapi import Depends,status,HTTPException
from jose import JWTError, jwt
from .import schema ,database,model
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')

SECRETE_KEY=settings.secret_key
ALGORITHM = settings.algorithm
ACESS_TOKEN_EXPIRE_MINUTES = settings.acess_token_expire_minutes


def create_acess_token(data:dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    
    encoded_jwt = jwt.encode(to_encode,SECRETE_KEY,algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token:str, credentials_exception):
    try:
        payload=jwt.decode(token,SECRETE_KEY,algorithms=[ALGORITHM])
        id:str=payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = schema.Tokendata(id=id)
    except JWTError:
        raise credentials_exception
    
    return token_data
    
def get_curent_user(token:str=Depends(oauth2_schema),db:Session = Depends(database.get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Could not validate credentials",headers={"WWW-Authenticate":"Bearer"})
    
    token = verify_access_token(token,credential_exception)
    user = db.query(model.Login).filter(model.Login.id == token.id).first()
    return user