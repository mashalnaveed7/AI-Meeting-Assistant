from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel


class PrivacyStatusWidget(QLabel):
    """
    Visual privacy status indicator.
    """

    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)

        self.setMinimumHeight(42)

        self.set_privacy_off()

    def set_privacy_on(self):

        self.setText(
            "🔒  PRIVACY MODE: ON  •  Screen Capture Protected"
        )

        self.setStyleSheet("""
            QLabel {
                background-color: #123524;
                color: #7CFFB2;
                border: 1px solid #2E8B57;
                border-radius: 10px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: bold;
            }
        """)

    def set_privacy_off(self):

        self.setText(
            "🔓  PRIVACY MODE: OFF"
        )

        self.setStyleSheet("""
            QLabel {
                background-color: #2A2F3A;
                color: #AAB2C0;
                border: 1px solid #414958;
                border-radius: 10px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: bold;
            }
        """)