import speech_recognition as sr


class SpeechToText:
    """
    Handles microphone input and converts speech into text.
    """

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):
        """
        Listen to the microphone and convert speech to text.

        Returns:
            str: Transcribed speech or an error message.
        """

        try:
            with self.microphone as source:

                print("Adjusting microphone for background noise...")

                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=1
                )

                print("Listening...")
                print("Speak now.")

                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=15
                )

            print("Processing speech...")

            text = self.recognizer.recognize_google(audio)

            print("You said:")
            print(text)

            return text

        except sr.WaitTimeoutError:

            print("No speech detected.")

            return ""

        except sr.UnknownValueError:

            print("Sorry, I could not understand the speech.")

            return ""

        except sr.RequestError as error:

            print("Speech recognition service error:")
            print(error)

            return ""

        except Exception as error:

            print("Unexpected microphone error:")
            print(error)

            return ""