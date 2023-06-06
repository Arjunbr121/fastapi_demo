from sqlalchemy import func
from ..import model,schema,utils,oauth2
from sqlalchemy.orm import Session
from fastapi import FastAPI,status,Response,HTTPException,Depends,APIRouter
from ..database import *
from typing import List,Optional

router = APIRouter(
    prefix='/posts',
    tags= ["Posts"]
)

# get method to get an individual data in DB
# .
@router.get("/{id}",response_model=schema.Post)
def get_post(id:int,db:Session = Depends(get_db),current_user : int= Depends(oauth2.get_curent_user)):
    post = db.query(model.Post).filter(model.Post.id == id).first()

    # post = db.query(model.Post,func.Count(model.Vote.post_id).label("Votes")).join(model.Vote, model.Vote.post_id == model.Post.id, isouter=True).group_by(model.Post.id).filter(model.Post.id == id).first()
    # val= model.Post.owner
    # print(val)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post of id {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{"details":f"post wit {id} not found"}
    # if post.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=" You are not authorized to acess this posts")
    
    return {"post details":post}

@router.get("/",response_model=List[schema.Postout])
def get(db:Session = Depends(get_db),current_user : int= Depends(oauth2.get_curent_user),limit:int = 10,skip:int =0, search:Optional[str]=""):
    #curser.exexute("""""")
    # post=curser.execute("""SELECT * FROM posts""")
    # print(post)
    # query = u"SELECT * FROM posts;"
    # curser.execute(query)
    # curser.execute("SELECT * FROM test;")
    # post=curser.fetchone()
    #query = u"UPDATE posts SET translated_text='%s', detected_language='%s' WHERE post_id=%s;"
    #vars = translation, detected_language['language'], str(post_id) # tuple
    # cur.execute(query, vars)
    # posts = db.query(model.Post).filter(model.Post.owner_id == current_user.id).all()
    # print(limit)
    # posts = db.query(model.Post).filter(model.Post.title.contains(search)).limit(limit).offset(skip).all()

    result = db.query(model.Post,func.Count(model.Vote.post_id).label("Votes")).join(model.Vote, model.Vote.post_id == model.Post.id, isouter=True).group_by(model.Post.id).filter(model.Post.title.contains(search)).limit(limit).offset(skip).all()
  
    return result
  



# post method to create a row in DB
# .
@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schema.Post)
def create_post(post:schema.CreatePost,db:Session = Depends(get_db),current_user : int= Depends(oauth2.get_curent_user)):
    # post_dict=post.dict()
    # post_dict['id']=randrange(0,1000)
    # my_post.append(post_dict)
    # new_posts = model.Post(title=post.title,content=post.content,published=post.published)
    # print(current_user.pasword)
    # print(current_user.id)
    new_posts = model.Post(owner_id=current_user.id, **post.dict())
    db.add(new_posts)
    db.commit()
    db.refresh(new_posts) 

    return new_posts


# put method to update  data in DB
# .
@router.put("/{id}")
def update_post(id:int,updated_post:schema.CreatePost,db:Session = Depends(get_db),current_user : int= Depends(oauth2.get_curent_user)):
    # index=find_index_post(id)
    # post_dict= post.dict()
    # post_dict['id']=id
    # my_post[index]=post_dict 
    print(current_user)
    post_query = db.query(model.Post).filter(model.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post not availabe")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=" You are not authorized to Update this posts")
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()

    return {"data": post_query.first()}
    
# delete method to delete an individual data in DB
# .
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session = Depends(get_db),current_user : int= Depends(oauth2.get_curent_user)):
    post_query = db.query(model.Post).filter(model.Post.id == id)
    post = post_query.first()

    print(current_user)
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post not availabe")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=" You are not authorized to delete this posts")
    

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
