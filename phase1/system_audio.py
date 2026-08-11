import pyaudiowpatch as pyaudio


class SystemAudioRecorder:
    """
    Captures audio coming from the Windows speaker output
    using WASAPI loopback.
    """

    def __init__(self):
        self.chunk = 1024
        self.audio = pyaudio.PyAudio()

        self.loopback_device = (
            self._find_loopback_device()
        )

        if self.loopback_device is None:
            raise RuntimeError(
                "Windows speaker loopback device was not found."
            )

    def _find_loopback_device(self):
        """
        Find the loopback device corresponding to the
        current Windows default output device.
        """

        wasapi_info = (
            self.audio.get_host_api_info_by_type(
                pyaudio.paWASAPI
            )
        )

        default_output_index = (
            wasapi_info["defaultOutputDevice"]
        )

        default_output = (
            self.audio.get_device_info_by_index(
                default_output_index
            )
        )

        default_name = default_output["name"]

        for index in range(
            self.audio.get_device_count()
        ):

            device = (
                self.audio.get_device_info_by_index(
                    index
                )
            )

            if not device.get(
                "isLoopbackDevice",
                False
            ):
                continue

            if device["name"].startswith(
                default_name
            ):
                return device

        return None

    def record(self, seconds=10):
        """
        Record Windows system audio for the
        requested number of seconds.

        Returns:
            bytes: Recorded PCM audio data.
        """

        device = self.loopback_device

        sample_rate = int(
            device["defaultSampleRate"]
        )

        channels = int(
            device["maxInputChannels"]
        )

        stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=channels,
            rate=sample_rate,
            input=True,
            input_device_index=device["index"],
            frames_per_buffer=self.chunk
        )

        frames = []

        try:

            for _ in range(
                int(
                    sample_rate
                    / self.chunk
                    * seconds
                )
            ):

                data = stream.read(
                    self.chunk,
                    exception_on_overflow=False
                )

                frames.append(data)

        finally:

            stream.stop_stream()
            stream.close()

        return (
            b"".join(frames)
        )

    def close(self):
        """
        Release the audio device.
        """

        if self.audio is not None:

            self.audio.terminate()

            self.audio = None