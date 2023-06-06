
from ..import model,schema,utils
from sqlalchemy.orm import Session
from fastapi import FastAPI,status,Response,HTTPException,Depends,APIRouter
from ..database import get_db

router = APIRouter(
     prefix= "/signup",
     tags= ["Users"]
)

@router.post('/',response_model=schema.Loginval)
def signup(user:schema.LoginPost,db:Session = Depends(get_db)):
    # if '@gmail.com' not in post.email:
    #     return {"Email Id Invaild "}
    # if len(post.password)<5 or '#' not in post.password:
    #     return {"Enter the password with more than 6 character and it should contain # for more security"}
    # user_exist=check_user_details(post,db)
    # print(user_exist)
    # if user_exist == None:
        # curser.execute("""INSER INTO LOGIN (firstname,lastname,email,password) VALUES (%s,%s,%s,%s) RETURING *"""(post.firstname,post.lastname,post.email,post.password))
        # user_exist=curser.fetchone()
        # conn.commit()

        hashed_password = utils.hash(user.pasword)
        user.pasword = hashed_password
        new_user = model.Login(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)    
        return new_user
    # else:  
    #     return {"status":"your account is already created"}


@router.get('/{id}',response_model=schema.Loginval) 
def signup(id:int,db:Session = Depends(get_db)):
    user = db.query(model.Login).filter(model.Login.id == id ).first()
    print(user)
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with {id} does not exist")
    
    return user

