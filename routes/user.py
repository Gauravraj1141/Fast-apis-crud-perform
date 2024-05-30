from fastapi import APIRouter
from models.user import User 
from config.db import conn 
from schema.user import SerializeDict, SerializeList
from bson import ObjectId
user = APIRouter() 

@user.get('/')
async def find_all_users():
    print(conn.local.user.find())
    return SerializeList(conn.local.user.find())

@user.post("/")
async def create_new_user(user: User):
    user_dict = dict(user)  # Convert Pydantic model to dictionary
    result = conn.local.user.insert_one(user_dict)  # Insert into MongoDB
    new_user = conn.local.user.find_one({"_id": result.inserted_id})  # Fetch the inserted document
    return SerializeDict(new_user)  

@user.put("/{id}")
async def update_user_detail(id, user: User):
    conn.local.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return SerializeDict(conn.local.user.find_one({"_id": ObjectId(id)}))


@user.delete("/{id}")
async def delete_user_detail(id):
    
    return SerializeDict(conn.local.user.find_one_and_delete({"_id": ObjectId(id)}))