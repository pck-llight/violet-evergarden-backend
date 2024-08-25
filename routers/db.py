import os
from pydantic import BaseModel
#routing
from fastapi import APIRouter

db = APIRouter(prefix='/db')

#몽고 DB 사용 모듈 추가
from pymongo import MongoClient, DESCENDING
from bson.json_util import dumps # bson -> json
from bson import ObjectId
client = MongoClient(os.getenv('MONGO_URI'))
mdb = client["violet"]

class Letter(BaseModel):
    sender: str
    receiver: str
    address: str
    letterName: str
    content: str

class Message(BaseModel):
    name: str
    date: str
    send: bool

class Request(BaseModel):
    sender: str
    receiver: str
    reason: str

@db.get("/")
def db_check():
    return {"db":"ok"}

lttr1 = Letter(sender="찬규", receiver="hi", address="asdfasdf", letterName="기모띠띠", content="야미노 사우르스")

#letter collections
@db.post('/letter')
def add_letter():
    mdb['letter'].insert_one({"dfasd":"adfas"})
    return 'okkokokokokok'


# @db.get('/letter')
# def del_letter():
#     mdb['letter'].delete_one()
#     return f"deleted: {lttr1.id, lttr1.content}"