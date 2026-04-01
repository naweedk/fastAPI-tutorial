from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
   return {"info": "This is about page"}

# Path parameters and query parameters are two different ways to pass data to an API endpoint.
@app.get("/user/{id}")
def get_user(id: int):
   return {"user_id": id}

@app.get("/search")
def search(q: str):
   return {"query": q}

@app.get("/items/{item_id}")
def get_items(item_id: int, discount: float = None):
   return {"item_id": item_id, "discount": discount}