from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
import re


class Feedback(BaseModel):
    name: str = Field(min_length = 2, max_length = 50)
    message: str = Field(min_length = 10, max_length = 500)

    @field_validator("message")
    def message_received(cls, value):
        plohie_slova = ["кринж","рофл","вайб"]
        patter = re.compile(rf"\b({'|'.join(plohie_slova)})\w*\b", re.IGNORECASE)

        if patter.search(value):
            raise ValueError("Использование недопустимых слов")
        return value

app = FastAPI()

feedbacks = []
@app.post("/feedback")
async def feedback(feedback: Feedback):
    feedbacks.append ({
        "name":feedback.name,
        "message":feedback.message
    })
    return {
        "message": f"Спасибо, {feedback.name}! Ваш отзыв сохранен."
    }