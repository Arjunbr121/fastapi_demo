from fastapi import FastAPI,status,Response,HTTPException,Depends
from fastapi.params import Body
import psycopg2
from psycopg2.extras import RealDictConnection
import time
from .import model,schema
from pydantic import BaseModel
from .database import engine,Sessionlocal,get_db
from sqlalchemy.orm import Session

model.Base.metadata.create_all(bind=engine)
app = FastAPI()


while True:
    try:
        conn=psycopg2.connect(host='localhost',database='app',user="postgres",password="Aarjunbr@131",cursor_factory=RealDictConnection)
        #curser= conn.cursor()
        print("Database connection was succesfully done!!!")
        break

    except Exception as error:
        print("The connection was not done")
        print("Errpr",error)
        time.sleep(2)


def check_user_details(post:schema.LoginPost,db:Session = Depends(get_db)):
    # curser.execute("""SELECT * FROM LOGIN WHERE EMAIL=%s AND PASSWORD=%s RETURNING *"""(email,password))
    # posts=curser.fetchone()
    posts = db.query(model.Login).filter(model.Login.email == post.email).all()
    # print(posts)
    if posts  != None:
        return 0
    else :
        return posts
    
#  @app.get('/')
#  def get_data(search:str=""):
#     # curser = conn.cursor()
#     # curser.execute("""SELECT * FROM LOGIN WHERE EMAIL=%s"""(search))
#     # post=curser.fetchone()

    #return{"email_details":"sucess"} 

@app.get("/sqlalchemy")
def test_posts(db:Session = Depends(get_db)):
     posts = db.query(model.Login).all()
     return{"staus":posts}


@app.post('/signup',response_model=schema.Loginval)
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
        new_user = model.Login(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)    
        return new_user
    # else: 
    #     return {"status":"your account is already created"}

    
@app.get('/login/')
def signup(post:schema.LoginPost,db:Session = Depends(get_db)):
    # curser.execute("""SELECT * FROM LOGIN WHERE EMAIL=%s AND PASSWORD=%s RETURNING *"""(post.email,post.password))
    # post=curser.fetchone()
    user_exist=0
    posts = 0
    print(posts)
    if posts != None:
        user_exist+=1

    if user_exist >0:
       return { "Status":"Login Succesfull Access Granted"}
    else:
       return { "Status":"Login erros  Access not Granted"}
