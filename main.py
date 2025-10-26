from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sample FastAPI App")

# For POST request
class Item(BaseModel):
    name: str
    value: int

# GET endpoint (static response)
@app.get("/hello")
def read_hello():
    return {"message": "Hello, World!"}

# POST endpoint (returns input with confirmation)
@app.post("/items")
def create_item(item: Item):
    return {"message": f"Item '{item.name}' with value {item.value} received successfully!"}
