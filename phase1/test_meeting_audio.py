import io
import wave

import speech_recognition as sr

from system_audio import SystemAudioRecorder


def main():

    print("=" * 50)
    print("MeetMind AI - Meeting Audio Test")
    print("=" * 50)

    recorder = SystemAudioRecorder()

    print()
    print("Listening to Windows system audio...")
    print("Ask another person to speak in Google Meet.")
    print("Recording for 10 seconds...")
    print()

    audio_data = recorder.record(
        seconds=10
    )

    recorder.close()

    # Save temporary WAV
    wav_buffer = io.BytesIO()

    # Get properties from the loopback device
    import pyaudiowpatch as pyaudio

    audio = pyaudio.PyAudio()

    wasapi_info = (
        audio.get_host_api_info_by_type(
            pyaudio.paWASAPI
        )
    )

    default_output = (
        audio.get_device_info_by_index(
            wasapi_info["defaultOutputDevice"]
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

        print(
            "Loopback device not found."
        )

        return

    sample_rate = int(
        loopback_device["defaultSampleRate"]
    )

    channels = int(
        loopback_device["maxInputChannels"]
    )

    audio.terminate()

    with wave.open(
        "meeting_audio_test.wav",
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

    print(
        "Audio captured successfully."
    )

    print(
        "Saved: meeting_audio_test.wav"
    )

    print()
    print(
        "Now converting speech to text..."
    )

    recognizer = sr.Recognizer()

    with sr.AudioFile(
        "meeting_audio_test.wav"
    ) as source:

        recorded_audio = (
            recognizer.record(source)
        )

    try:

        text = (
            recognizer.recognize_google(
                recorded_audio
            )
        )

        print()
        print("=" * 50)
        print("DETECTED SPEECH:")
        print(text)
        print("=" * 50)

    except sr.UnknownValueError:

        print()
        print(
            "Speech was captured, but "
            "Google Speech Recognition "
            "could not understand it."
        )

    except sr.RequestError as error:

        print()
        print(
            "Speech recognition service error:"
        )

        print(error)


if __name__ == "__main__":
    main()