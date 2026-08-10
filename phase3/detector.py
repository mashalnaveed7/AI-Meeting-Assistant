import json
from pathlib import Path

import psutil


class AIAssistantDetector:
    """
    Detects running processes that match the configured
    list of known AI assistant process names.
    """

    def __init__(self):

        self.config_file = (
            Path(__file__).resolve().parent
            / "known_apps.json"
        )

        self.known_tools = []

        self.load_known_tools()

    def load_known_tools(self):
        """
        Load known AI assistant process names
        from known_apps.json.
        """

        try:

            with open(
                self.config_file,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            self.known_tools = [
                tool.lower()
                for tool in data.get(
                    "known_ai_tools",
                    []
                )
            ]

        except Exception as error:

            print(
                "Error loading known AI tools:"
            )

            print(error)

            self.known_tools = []

    def get_running_processes(self):
        """
        Return currently running Windows processes
        including PID, process name, and command line.
        """

        processes = []

        for process in psutil.process_iter(
            ["pid", "name", "cmdline"]
        ):

            try:

                pid = process.info["pid"]

                name = process.info["name"]

                cmdline = process.info.get(
                    "cmdline"
                )

                if name:

                    processes.append(
                        {
                            "pid": pid,
                            "name": name,
                            "cmdline": cmdline or []
                        }
                    )

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess
            ):

                continue

        return processes

    def detect(self):
        """
        Scan running processes and detect known
        AI assistant processes.

        Detection works using:

        1. Configured process names
        2. The project's safe mock AI assistant
           for testing purposes
        """

        detected = []

        running_processes = (
            self.get_running_processes()
        )

        for process in running_processes:

            process_name = (
                process["name"].lower()
            )

            # -------------------------------------------------
            # METHOD 1:
            # Normal configured process-name detection
            # -------------------------------------------------

            if process_name in self.known_tools:

                detected.append(
                    {
                        "pid": process["pid"],
                        "name": process["name"]
                    }
                )

                continue

            # -------------------------------------------------
            # METHOD 2:
            # Safe mock AI assistant detection
            # -------------------------------------------------

            command_line = " ".join(
                process.get(
                    "cmdline",
                    []
                )
            ).lower()

            if (
                process_name == "python.exe"
                and "mock_ai_assistant.py"
                in command_line
            ):

                detected.append(
                    {
                        "pid": process["pid"],
                        "name": "mock_ai_assistant.exe"
                    }
                )

        return detected

    def is_ai_tool_detected(self):
        """
        Return True if at least one known AI
        assistant process is currently running.
        """

        results = self.detect()

        return len(results) > 0

    def get_detection_summary(self):
        """
        Return a simple summary of the current scan.
        """

        results = self.detect()

        if not results:

            return {
                "detected": False,
                "count": 0,
                "tools": []
            }

        return {
            "detected": True,
            "count": len(results),
            "tools": results
        }


if __name__ == "__main__":

    detector = AIAssistantDetector()

    print("=" * 50)

    print(
        "AI ASSISTANT DETECTION TEST"
    )

    print("=" * 50)

    results = detector.detect()

    if results:

        print(
            "WARNING: AI assistant detected!"
        )

        for item in results:

            print(
                f"PID: {item['pid']} | "
                f"Process: {item['name']}"
            )

    else:

        print(
            "No known AI assistant detected."
        )