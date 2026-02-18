from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()

class User(BaseModel):
    name: str
    age: int


external_date = {
    "name" : "Dima",
    "age" : 20,
}

user = User(**external_date)

@app.post("/users")
async def is_adult(user : User):
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