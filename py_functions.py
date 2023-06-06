

def check_user_details(username,password,cnxn):
    query = 'Select * from USER_CREDS where email='+"'"+str(username)+"'"+'and Password'+"'"+str(password)+"'"
    df=pd.read_sql(query,cnxn)
    return df.shape[0]

def check_user_exist(email,cnxn):
    query = 'Select * from USER_CREDS where email='+"'"+str(email)+"'"
    df=pd.read_sql(query,cnxn)
    return df.shape[0]

def signup_data(firstname,lastname,email,password):
    query = "INSER INTO uSER_CREDS"\
            "VALUES ("+"'"+str(firstname)+"'"+","+str(lastname)+"'"+","+str(email)+"'"+","+str(password)+"'"+")"
    print(query)
    """ df=pd.read_sql(query,cnxn) """
    return query
