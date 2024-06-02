from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    plu: int


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://192.168.1.2",
    "http://192.168.1.2:5173",
    "192.168.1.2",
    "192.168.1.3",
    "192.168.1.4",
    "192.168.1.5",
    "192.168.1.6",
    "192.168.1.7",
    "192.168.1.8",
    "192.168.1.9",
    "192.168.1.10",
    "192.168.1.11",
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
    return {"message": "The duck flew over the pond at midnight."}


@app.post("/")
async def root(item: Item):
    item_dict = item.dict()
    if item.name == "fish":
        item_dict.update({"name": "halibut"})
        item_dict.update({"description": "A fish that lives in the water"})
        item_dict.update({"plu": 123})
    return item_dict


@app.post("/items/")
async def create_item(item: Item):
    table = {
        "columns": [
            {"title": "Name", "field": "name", "width": 150},
            {
                "title": "Age",
                "field": "age",
                "hozAlign": "left",
                "formatter": "progress",
            },
            {"title": "Favourite Color", "field": "col"},
            {
                "title": "Date Of Birth",
                "field": "dob",
                "sorter": "date",
                "hozAlign": "center",
            },
        ],
        "rows": [
            {
                "id": 1,
                "name": "Oli Bob",
                "progress": 12,
                "gender": "male",
                "rating": 1,
                "col": "red",
                "dob": "19/02/1984",
                "car": 1,
            },
            {
                "id": 2,
                "name": "Mary May",
                "progress": 1,
                "gender": "female",
                "rating": 2,
                "col": "blue",
                "dob": "14/05/1982",
                "car": "true",
            },
            {
                "id": 3,
                "name": "Christine Lobowski",
                "progress": 42,
                "gender": "female",
                "rating": 0,
                "col": "green",
                "dob": "22/05/1982",
                "car": "true",
            },
            {
                "id": 4,
                "name": "Brendon Philips",
                "progress": 100,
                "gender": "male",
                "rating": 1,
                "col": "orange",
                "dob": "01/08/1980",
            },
            {
                "id": 5,
                "name": "Margret Marmajuke",
                "progress": 16,
                "gender": "female",
                "rating": 5,
                "col": "yellow",
                "dob": "31/01/1999",
            },
            {
                "id": 6,
                "name": "Frank Harbours",
                "progress": 38,
                "gender": "male",
                "rating": 4,
                "col": "red",
                "dob": "12/05/1966",
                "car": 1,
            },
        ],
    }
    return table
