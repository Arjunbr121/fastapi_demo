import uvicorn
from fastapi import FastAPI
import py_functions
import config
import pyodbc
import json

app = FastAPI()


def connect(pwd):
     driver = config.DRIVER
     server = config.SERVER
     database= config.DATABASE
     uid = config.UID
     pwd = config.PWD
     trust = config.TRUST
     con_string = f'DRIVER ={driver};SERVER = {server};DATABASE = {database};UID = {uid};PWD={pwd}'
     cnxn=pyodbc.connect(con_string)
     cnxn.autocommit = True
     cursor = cnxn.cursor()
     print("Connectin succesfull with the database")
     return cnxn,cursor


with open('sql/password.json') as f:
       {"password ":"xyz"} 
data=json.load(f)
pwd=data['password']

cnxn,cursor  =connect_db(pwd)

@app.get('/')
def get_data(search:str =""):
    df= py_functions.fetch_data(search,cnxn)
    return df.to_dict('r')

@app.post('/signup/')
def signup(firstname:str, lastname:str,email:str,password:str):
    if '@gmail.com' not in email:
        return {"Email Id Invaild "}
    if len(password)<5 or '#' not in password:
        return {"Enter the password with more than 6 character and it should contain # for more security"}
    user_exist = py_functions.check_user_exist(email,cnxn)
    if user_exist == 0:
        signup_query = py_functions.signupdata(firstname,lastname,email,password)
        cursor.execute(signup_query)
        return {"status":"Signed UP already please login with the same creds"}
    else:
        return {"status": " Email id already exist."}
    
@app.post('/login/')
def signup(email:str,password:str):
   user_exist = py_functions.check_user_details(email,password,cnxn) 
   if user_exist >0:
       return { "Status":"Login Succesfull Access Granted"}
   else:
       return { "Status":"Login erros  Access not Granted"}


if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1",port=8000) 