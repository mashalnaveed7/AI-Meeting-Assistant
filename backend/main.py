import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq

load_dotenv()

app = FastAPI(
    title="MeetMind AI Backend",
    version="1.0.0"
)

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError(
        "GROQ_API_KEY is not configured on the server."
    )

client = Groq(api_key=api_key)

MODEL = "llama-3.1-8b-instant"


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "status": "online",
        "service": "MeetMind AI Backend"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    if len(question) > 4000:
        raise HTTPException(
            status_code=400,
            detail="Question is too long."
        )

    try:

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI meeting assistant. "
                        "Answer questions clearly, accurately, "
                        "and concisely. "
                        "Give practical answers suitable for "
                        "a student or professional meeting."
                    )
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=0.3,
            max_tokens=500
        )

        answer = response.choices[0].message.content

        return {
            "answer": answer.strip()
        }

    except Exception as error:

        print("Groq error:")
        print(error)

        raise HTTPException(
            status_code=500,
            detail="AI service is temporarily unavailable."
        )