# Simplified test_api/main.py

from fastapi import FastAPI

app = FastAPI(title="Simplified Sample FastAPI App")

# GET endpoint (static response) - Stays the same
@app.get("/hello")
def read_hello():
    return {"message": "Hello, World!"}

# --- SIMPLIFIED POST ENDPOINT ---
# Now takes a simple query parameter instead of a JSON body
@app.post("/items")
def create_item_simple(item_name: str):
    # No Pydantic validation needed here
    return {"message": f"Item '{item_name}' received successfully!"}

# You can keep the old endpoint commented out or remove it
# class Item(BaseModel):
#     name: str
#     value: int
# @app.post("/items_old")
# def create_item(item: Item):
#     return {"message": f"Item '{item.name}' with value {item.value} received successfully!"}