from fastapi import FastAPI, HTTPException, status, Response
from fastapi.params import Body
from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional

app = FastAPI()

my_posts = [{"id": 1, "name": "Ninh Binh"}, 
            {"id": 2, "name": "Dak Lak"}]

class District(BaseModel):
    id: Optional[int] = None
    name: str

def find_post(id: int) -> District:
    for post in my_posts:
        if post['id'] == id:
            return post
    return None
        

def find_index_post(id: int) -> int:
    for i, post in enumerate(my_posts):
        if post['id'] == id:
            return i
    return None

@app.get("/posts")
def get_posts():
    return {"Posts": my_posts}

@app.get("/post/lastest")
def get_last_post():
    return {"Lastest post": my_posts[len(my_posts)-1]}

@app.get('/post/{id}')
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not found post {id}")
    return {'Post': post}

@app.post("/post", status_code=status.HTTP_201_CREATED)
def create_post(post: District):
    my_posts.append(post.model_dump())
    return get_last_post()

@app.put("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def update_post(id: int, post: District):
    post_index = find_index_post(id)
    
    if not post_index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Not found post {id}")
    
    post.id = id
    my_posts[post_index] = post
    return f"Update sucessfull"

@app.delete("/post/{id}")
def delete_post(id: int):
    post_index = find_index_post(id)

    if not post_index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not found post {id}")
    my_posts.pop(post_index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)




# @app.post("/post") 
# def create_post(paras: Data):
#     return f"Title: {paras.title}, Content: {paras.content}, Pushlish: {paras.pushlish}, Number: {paras.number}"
