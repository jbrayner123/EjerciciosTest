from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Testing Starter API")

class Item(BaseModel):
    id: int
    name: str

# In-memory "DB"
ITEMS = {
    1: Item(id=1, name="Alpha"),
    2: Item(id=2, name="Beta"),
}

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = ITEMS.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    if item.id in ITEMS:
        raise HTTPException(status_code=400, detail="Item already exists")
    ITEMS[item.id] = item
    return item
