from fastapi import FastAPI
from pydantic import BaseModel

feedback_message = []
class Feedback(BaseModel):
    name: str
    message: str

app = FastAPI()
@app.post("/feedback")
async def feedback(feedback: Feedback):
    feedback_message.append ({
        "name":feedback.name,
        "message":feedback.message
    })
    return {
        "message": f"Feedback received. Thank you,{feedback.name}!"
    }