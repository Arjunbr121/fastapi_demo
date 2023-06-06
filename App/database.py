from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictConnection
from .config import settings

# SQLALCHEMY_DATABASE_URL =f'postgresql://drivexdb:vjsTrUcM3JrArkHkbtp@pg-db.sirpi.co.in/postgres'

SQLALCHEMY_DATABASE_URL =f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 

def get_db():
    db=Sessionlocal() 
    try:
        yield db
    finally:
        db.close()

# connecting with the database for postgress where we use query
# .
try:
    conn=psycopg2.connect(host='localhost',database='app',user='postgres',password='Aarjunbr@131',
                          cursor_factory=RealDictConnection)    
    #curser = conn.Cursor()
    print("Database connection was succesfully done!!!")
        
except Exception as error:
    print("The connection was not done")
    print("Error",error)
   

# Base = declarative_base()
# PG_NAME=drivexdb
# PG_USER=postgres
# PG_PASSWORD=vjsTrUcM3JrArkHkbtp
# PG_PORT=5432
# PG_HOST=pg-db.sirpi.co.in

# 509747391536
# DEAPA4768A