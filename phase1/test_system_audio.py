import pyaudiowpatch as pyaudio
import wave

OUTPUT_FILE = "system_audio_test.wav"

CHUNK = 1024
RECORD_SECONDS = 10


def record_system_audio():
    print("=" * 50)
    print("MeetMind AI - System Audio Test")
    print("=" * 50)

    p = pyaudio.PyAudio()

    # WASAPI host
    wasapi_info = p.get_host_api_info_by_type(
        pyaudio.paWASAPI
    )

    # Get default Windows output device
    default_speakers = p.get_device_info_by_index(
        wasapi_info["defaultOutputDevice"]
    )

    print("\nDefault output device:")
    print(default_speakers["name"])

    # Find loopback device for the speakers
    loopback_device = None

    for i in range(p.get_device_count()):
        device = p.get_device_info_by_index(i)

        if (
            device["isLoopbackDevice"]
            and device["name"].startswith(
                default_speakers["name"]
            )
        ):
            loopback_device = device
            break

    if loopback_device is None:
        print("\nERROR: Loopback device not found.")
        p.terminate()
        return

    print("\nLoopback device found:")
    print(loopback_device["name"])

    sample_rate = int(loopback_device["defaultSampleRate"])
    channels = int(loopback_device["maxInputChannels"])

    print("\nRecording system audio for 10 seconds...")
    print("Play a YouTube video or Google Meet audio now.")
    print("Speak through Google Meet during the test.")

    stream = p.open(
        format=pyaudio.paInt16,
        channels=channels,
        rate=sample_rate,
        input=True,
        input_device_index=loopback_device["index"],
        frames_per_buffer=CHUNK
    )

    frames = []

    for _ in range(
        int(sample_rate / CHUNK * RECORD_SECONDS)
    ):
        data = stream.read(
            CHUNK,
            exception_on_overflow=False
        )
        frames.append(data)

    print("\nRecording finished.")

    stream.stop_stream()
    stream.close()

    p.terminate()

    with wave.open(
        OUTPUT_FILE,
        "wb"
    ) as wf:

        wf.setnchannels(channels)
        wf.setsampwidth(
            p.get_sample_size(pyaudio.paInt16)
        )
        wf.setframerate(sample_rate)
        wf.writeframes(
            b"".join(frames)
        )

    print("\nSaved:")
    print(OUTPUT_FILE)
    print("\nSystem audio capture test completed.")


if __name__ == "__main__":
    record_system_audio()