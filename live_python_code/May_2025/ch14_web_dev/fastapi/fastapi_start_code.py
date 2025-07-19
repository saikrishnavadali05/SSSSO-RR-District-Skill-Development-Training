from fastapi import FastAPI, Path, Query, Body, Depends, status
from pydantic import BaseModel
from typing import Optional
from fastapi import Path
import uvicorn

app = FastAPI()


# Example 1: Basic endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}


@app.get("/items/{item_id}")
def read_item(item_id: int = Path(..., description="The ID of the item to get")):
    return {"item_id": item_id}

@app.get("/search/")
def search(q: Optional[str] = Query(None, max_length=50)):
    return {"query": q}

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}

@app.get("/async/")
async def async_endpoint():
    return {"message": "This is async"}

@app.get("/defaults/")
def defaults(limit: int = 10, offset: int = 0):
    return {"limit": limit, "offset": offset}

@app.api_route("/multi-method/", methods=["GET", "POST"])
def multi_method():
    return {"message": "Supports GET and POST"}

def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 10):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/dependency/")
def read_dependency(commons: dict = Depends(common_parameters)):
    return commons

@app.post("/items-with-status/", status_code=status.HTTP_201_CREATED)
def create_item_with_status(item: Item):
    return item

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000, log_level="info")