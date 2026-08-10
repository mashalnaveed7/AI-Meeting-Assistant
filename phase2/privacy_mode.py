import ctypes
import sys


class PrivacyMode:
    """
    Controls whether the application window is excluded
    from supported Windows screen-capture APIs.
    """

    WDA_NONE = 0x00000000
    WDA_EXCLUDEFROMCAPTURE = 0x00000011

    def __init__(self, window):
        self.window = window
        self.enabled = False

    def enable(self):
        """
        Enable privacy mode.

        The application remains visible on the user's monitor,
        but Windows will attempt to exclude it from supported
        screen-capture APIs.
        """

        if sys.platform != "win32":
            return False

        try:
            hwnd = int(self.window.winId())

            result = ctypes.windll.user32.SetWindowDisplayAffinity(
                hwnd,
                self.WDA_EXCLUDEFROMCAPTURE
            )

            if result:
                self.enabled = True
                return True

            return False

        except Exception as error:
            print("Privacy mode error:")
            print(error)

            return False

    def disable(self):
        """
        Disable privacy mode and return to normal window capture.
        """

        if sys.platform != "win32":
            return False

        try:
            hwnd = int(self.window.winId())

            result = ctypes.windll.user32.SetWindowDisplayAffinity(
                hwnd,
                self.WDA_NONE
            )

            if result:
                self.enabled = False
                return True

            return False

        except Exception as error:
            print("Privacy mode error:")
            print(error)

            return False

    def toggle(self):
        """
        Toggle privacy mode.
        """

        if self.enabled:
            return self.disable()

        return self.enable()

    def is_enabled(self):
        """
        Return current privacy mode state.
        """

        return self.enabled