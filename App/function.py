from pydantic import BaseModel
from random import randrange
import psycopg2
from fastapi import FastAPI,status,Response,HTTPException
from fastapi.params import Body
from psycopg2.extras import RealDictConnection
from sqlalchemy import URL, create_engine

app= FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool=True
   
PG_NAME='drivexdb'
PG_USER='postgres'
PG_PASSWORD='vjsTrUcM3JrArkHkbtp'
PG_PORT=5432
PG_HOST='pg-db.sirpi.co.in'

url_object = URL.create(
    "postgresql+pg8000",
    username="postgres",
    password="vjsTrUcM3JrArkHkbtp",  # plain (unescaped) text
    host='pg-db.sirpi.co.in',
    database="postgres",
)
engine = create_engine(url_object)
engine = create_engine("postgresql://scott:tiger@pg-db.sirpi.co.in/postgres")
engine.connect(host='pg-db.sirpi.co.in',database='postgres',user='drivexdb',password='vjsTrUcM3JrArkHkbtp',
                          cursor_factory=RealDictConnection)
try:
    conn=psycopg2.connect(host='pg-db.sirpi.co.in',database='postgres',user='drivexdb',password='vjsTrUcM3JrArkHkbtp',
                          cursor_factory=RealDictConnection)
    cursrr = conn.cursor()
    #cursor = conn.commit()
    
    print("Database connection was succesfully done!!!")

except Exception as error:
    print("The connection was not done")
    print("Error",error)