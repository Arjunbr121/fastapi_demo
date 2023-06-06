from fastapi import APIRouter, Depends,status, HTTPException
from sqlalchemy.orm import Session
from ..import database,schema,model,utils ,oauth2


router = APIRouter(tags=['Authentication']
)

@router.post('/login',response_model=schema.Token)
def  login(user_credentials:schema.UserVal, db:Session = Depends(database.get_db)):
    user = db.query(model.Login).filter(model.Login.email == user_credentials.email).first()
    # print(user)

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'Invalid credentials')

    if not utils.verify(user_credentials.pasword,user.pasword):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"invalid credentials")
    
    # return token

    access_token = oauth2.create_acess_token(data = {"user_id":user.id})
    return{"acess_token":access_token,"token_type":"bearer"}
