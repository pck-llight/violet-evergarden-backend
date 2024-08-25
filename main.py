#fastapi 모듈 추가
from fastapi import FastAPI, HTTPException, APIRouter

#add routing file
from routers.db import db

app = FastAPI()
app.include_router(db)

@app.get('/')
def home():
    return {'msg' : 'Main'}
