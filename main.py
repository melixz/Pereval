from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    email: str
    fam: str
    name: str
    otc: str
    phone: str

class Coords(BaseModel):
    latitude: str
    longitude: str
    height: str

class Image(BaseModel):
    data: str
    title: str

class Level(BaseModel):
    winter: str
    summer: str
    autumn: str
    spring: str

class Item(BaseModel):
    beauty_title: str
    title: str
    other_titles: str
    connect: str
    add_time: str
    user: User
    coords: Coords
    level: Level
    images: List[Image]

@app.post("/submitData/")
async def submit_data(item: Item):
    return {"item": item}


uvicorn.run(app, host="127.0.0.1", port=8000)

