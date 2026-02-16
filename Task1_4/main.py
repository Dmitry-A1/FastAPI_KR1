from models import User
from fastapi import FastAPI
user1 = User(id=1,name="Дима Ануров")
app = FastAPI()

@app.get("/users")
async def get_users():
    return {
        "id":user1.id ,
        "name":user1.name
    }