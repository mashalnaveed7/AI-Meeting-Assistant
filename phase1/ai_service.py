import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


class AIService:
    """
    Handles communication with the Groq LLM.
    """

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY was not found in the .env file."
            )

        self.client = Groq(
            api_key=api_key
        )

        self.model = "llama-3.1-8b-instant"

    def get_answer(self, question):
        """
        Send a question to the LLM and return its answer.
        """

        if not question.strip():
            return "Please provide a question."

        try:

            response = self.client.chat.completions.create(

                model=self.model,

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

            return answer.strip()

        except Exception as error:

            print("AI service error:")
            print(error)

            return (
                "Sorry, I could not generate an answer "
                "right now."
            )