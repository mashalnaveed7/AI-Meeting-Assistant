import json
import urllib.request
import urllib.error


class AIService:
    """
    Connects MeetMind AI to the MeetMind backend.
    The Groq API key is kept on the backend and is
    never stored inside the desktop application.
    """

    def __init__(self):

        self.backend_url = "http://127.0.0.1:8000/ask"

    def get_answer(self, question):
        """
        Send a question to the MeetMind backend
        and return the AI-generated answer.
        """

        if not question or not question.strip():

            return "Please provide a question."

        try:

            data = json.dumps({
                "question": question.strip()
            }).encode("utf-8")

            request = urllib.request.Request(
                self.backend_url,
                data=data,
                headers={
                    "Content-Type": "application/json"
                },
                method="POST"
            )

            with urllib.request.urlopen(
                request,
                timeout=30
            ) as response:

                response_data = json.loads(
                    response.read().decode("utf-8")
                )

            answer = response_data.get(
                "answer",
                ""
            )

            if answer:

                return answer.strip()

            return "No answer was returned by the AI service."

        except urllib.error.URLError as error:

            print("MeetMind backend connection error:")
            print(error)

            return (
                "MeetMind AI backend is not available.\n\n"
                "Please make sure the MeetMind backend "
                "is running."
            )

        except Exception as error:

            print("AI service error:")
            print(error)

            return (
                "Sorry, I could not generate an answer "
                "right now."
            )