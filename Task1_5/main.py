from pydantic import BaseModel
from fastapi import FastAPI

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post("/users")
async def is_adult(user: User):
    if user.age >= 18:
        return {
            "name":user.name,
            "age":user.age,
            "is_adult":True
        }
    else:
        return {
            "name":user.name,
            "age":user.age,
            "is_adult":False
        }