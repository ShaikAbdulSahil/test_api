# Updated test_api/main.py (Simpler GET with Path Parameter)

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Super Simple Sample FastAPI App")

# GET endpoint (static response) - Stays the same
@app.get("/hello")
def read_hello():
    return {"message": "Hello, World!"}

# --- NEW: Simple GET endpoint with a path parameter ---
@app.get("/check_prime/{number}")
def check_if_prime(number: int):
    """Checks if a given integer is a prime number."""
    if number < 2:
        # You could return False or raise an error, let's raise for testing
        raise HTTPException(status_code=400, detail="Number must be 2 or greater.")
    
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 1:
            is_prime = False
            break
            
    return {"number": number, "is_prime": is_prime}

# --- Keep the old POST endpoint commented out or remove it ---
# class Item(BaseModel):
#     name: str
#     value: int
# @app.post("/items")
# def create_item_simple(item_name: str):
#     return {"message": f"Item '{item_name}' received successfully!"}
