import speech_recognition as sr

from PySide6.QtCore import QThread, Signal

from phase1.system_audio import SystemAudioRecorder


class MeetingAudioWorker(QThread):
    """
    Captures Google Meet/system audio and converts
    the detected speech into text.
    """

    transcription_ready = Signal(str)
    listening_status = Signal(str)

    def __init__(self):
        super().__init__()

        self.running = True

        self.recognizer = sr.Recognizer()

    def run(self):

        try:

            recorder = SystemAudioRecorder()

        except Exception as error:

            self.listening_status.emit(
                "SYSTEM AUDIO ERROR"
            )

            print(
                "System audio initialization error:"
            )

            print(error)

            return

        self.listening_status.emit(
            "MEETING AUDIO LISTENING"
        )

        try:

            while self.running:

                self.listening_status.emit(
                    "LISTENING TO MEETING"
                )

                audio_data = recorder.record(
                    seconds=10
                )

                if not self.running:
                    break

                self.listening_status.emit(
                    "PROCESSING MEETING AUDIO"
                )

                text = self._speech_to_text(
                    audio_data,
                    recorder
                )

                if text:

                    self.transcription_ready.emit(
                        text
                    )

        except Exception as error:

            print(
                "Meeting audio worker error:"
            )

            print(error)

            self.listening_status.emit(
                "MEETING AUDIO ERROR"
            )

        finally:

            recorder.close()

    def _speech_to_text(
        self,
        audio_data,
        recorder
    ):

        try:

            import wave
            import io

            import pyaudiowpatch as pyaudio

            audio = pyaudio.PyAudio()

            wasapi_info = (
                audio.get_host_api_info_by_type(
                    pyaudio.paWASAPI
                )
            )

            default_output = (
                audio.get_device_info_by_index(
                    wasapi_info[
                        "defaultOutputDevice"
                    ]
                )
            )

            loopback_device = None

            for index in range(
                audio.get_device_count()
            ):

                device = (
                    audio.get_device_info_by_index(
                        index
                    )
                )

                if (
                    device.get(
                        "isLoopbackDevice",
                        False
                    )
                    and device["name"].startswith(
                        default_output["name"]
                    )
                ):

                    loopback_device = device
                    break

            if loopback_device is None:

                audio.terminate()

                return ""

            sample_rate = int(
                loopback_device[
                    "defaultSampleRate"
                ]
            )

            channels = int(
                loopback_device[
                    "maxInputChannels"
                ]
            )

            audio.terminate()

            wav_buffer = io.BytesIO()

            with wave.open(
                wav_buffer,
                "wb"
            ) as wav_file:

                wav_file.setnchannels(
                    channels
                )

                wav_file.setsampwidth(
                    2
                )

                wav_file.setframerate(
                    sample_rate
                )

                wav_file.writeframes(
                    audio_data
                )

            wav_buffer.seek(0)

            with sr.AudioFile(
                wav_buffer
            ) as source:

                recorded_audio = (
                    self.recognizer.record(
                        source
                    )
                )

            text = (
                self.recognizer.recognize_google(
                    recorded_audio
                )
            )

            return text.strip()

        except sr.UnknownValueError:

            return ""

        except sr.RequestError as error:

            print(
                "Speech recognition error:"
            )

            print(error)

            return ""

        except Exception as error:

            print(
                "Meeting speech conversion error:"
            )

            print(error)

            return ""

    def stop(self):

        self.running = False

        self.wait()