from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Testing Starter API")

class Item(BaseModel):
    id: int
    name: str

class PriceResponse(BaseModel):
    usd: float
    rate: float
    cop: float

# In-memory "DB"
ITEMS = {
    1: Item(id=1, name="Alpha"),
    2: Item(id=2, name="Beta"),
}

# Dependency for exchange rate (USD -> COP)
def get_exchange_rate() -> float:
    """Returns the current USD to COP exchange rate."""
    return 4000.0  # Default rate

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

# EXERCISE 1: GET /items with optional filter ?q=
@app.get("/items", response_model=List[Item])
def list_items(q: Optional[str] = None):
    """
    Get all items, optionally filtered by name (case-insensitive).
    
    Args:
        q: Optional query string to filter items by name
    
    Returns:
        List of items matching the filter criteria
    """
    items_list = list(ITEMS.values())
    
    if q is None:
        return items_list
    
    # Filter items by name (case-insensitive)
    filtered_items = [
        item for item in items_list 
        if q.lower() in item.name.lower()
    ]
    
    return filtered_items

# EXERCISE 2: GET /price/{usd} with mocked dependency
@app.get("/price/{usd}", response_model=PriceResponse)
def get_price(usd: float, rate: float = Depends(get_exchange_rate)):
    """
    Convert USD to COP using the exchange rate from dependency.
    
    Args:
        usd: Amount in USD to convert
        rate: Exchange rate (injected via dependency)
    
    Returns:
        Object with usd, rate, and cop values
    
    Raises:
        HTTPException: If usd is negative
    """
    if usd < 0:
        raise HTTPException(
            status_code=400, 
            detail="USD amount must be non-negative"
        )
    
    cop = usd * rate
    
    return PriceResponse(
        usd=usd,
        rate=rate,
        cop=cop
    )