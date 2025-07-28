from typing import Union
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from pymongo import MongoClient

app = FastAPI()

conn = MongoClient("mongodb+srv://Phoenix:Phoenix9009@shotay.h4uaiou.mongodb.net/")
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        print(doc)
        id = doc.get("_id")
        note = doc.get("note")
        print(f"ID: {id}, Note: {note}")
        newDocs.append({"id": id, "note": note})

    return templates.TemplateResponse("index.html", {"request": request, "notes": newDocs})


# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse(
#         request=request, name="item.html", context={"id": id}
#     )