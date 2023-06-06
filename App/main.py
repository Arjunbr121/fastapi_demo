from fastapi import FastAPI
from .import model
from .database import engine
from .routers import post,user,auth,vote
from fastapi.middleware.cors import CORSMiddleware
model.Base.metadata.create_all(bind=engine)

app= FastAPI()    

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=['*'],
    allow_headers = ['*']
)

# my_post=[{"title":"title of the post 1","content":"content of post 1","id":1},
#          {"title":"favaorite foods ","content":"i like piza","id":2}] 
# def find_post(id):
#     for p in my_post:
#         if p['id']==id:
#             return p
      
# def find_index_post(id):
#     for i,p in enumerate(my_post):
#         if p['id']==id:
#             return i
# basic blue print how to write
# .
# @app.get("/sqlalchemy")
# def test_posts(db:Session = Depends(get_db)):
#     posts = db.query(model.Post).all()
#     return{"staus":posts}

@app.get("/")
def root():
    return {"message": "Welcome to api!!! "}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)



