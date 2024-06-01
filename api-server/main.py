from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    plu: int

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://192.168.1.7:5173",
    "192.168.1.7:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "The duck flew over the pond at midnight."
    }

@app.post("/")
async def root(item: Item):
    item_dict = item.dict()
    if item.name == "fish":
        item_dict.update({ "name": "halibut" })
        item_dict.update({ "description": "A fish that lives in the water" })
        item_dict.update({ "plu":  123 })
    return item_dict
