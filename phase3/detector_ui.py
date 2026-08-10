import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QListWidget,
    QMessageBox
)

from detector import AIAssistantDetector


class DetectionWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.detector = (
            AIAssistantDetector()
        )

        self.setWindowTitle(
            "AI Assistant Detection System"
        )

        self.setMinimumSize(
            850,
            650
        )

        self.create_ui()

        self.run_scan()

    def create_ui(self):

        central_widget = QWidget()

        self.setCentralWidget(
            central_widget
        )

        central_widget.setStyleSheet("""
            QWidget {
                background-color: #10141C;
                color: #E8ECF3;
                font-family: "Segoe UI";
            }
        """)

        main_layout = QVBoxLayout()

        main_layout.setContentsMargins(
            30,
            25,
            30,
            25
        )

        main_layout.setSpacing(
            18
        )

        central_widget.setLayout(
            main_layout
        )

        # HEADER
        header_layout = QHBoxLayout()

        title_layout = QVBoxLayout()

        title = QLabel(
            "AI ASSISTANT DETECTOR"
        )

        title.setStyleSheet("""
            QLabel {
                color: #F4F7FB;
                font-size: 27px;
                font-weight: 700;
            }
        """)

        subtitle = QLabel(
            "Monitor running applications for known AI assistant tools"
        )

        subtitle.setStyleSheet("""
            QLabel {
                color: #8E99AA;
                font-size: 13px;
            }
        """)

        title_layout.addWidget(
            title
        )

        title_layout.addWidget(
            subtitle
        )

        header_layout.addLayout(
            title_layout
        )

        header_layout.addStretch()

        self.status_label = QLabel(
            "● READY"
        )

        self.status_label.setAlignment(
            Qt.AlignCenter
        )

        self.status_label.setMinimumWidth(
            150
        )

        self.status_label.setStyleSheet("""
            QLabel {
                background-color: #202733;
                color: #71D79A;
                border: 1px solid #334052;
                border-radius: 18px;
                padding: 8px 16px;
                font-size: 12px;
                font-weight: bold;
            }
        """)

        header_layout.addWidget(
            self.status_label
        )

        main_layout.addLayout(
            header_layout
        )

        # RESULT CARD
        result_card = QFrame()

        result_card.setStyleSheet("""
            QFrame {
                background-color: #181E28;
                border: 1px solid #293241;
                border-radius: 14px;
            }
        """)

        result_layout = QVBoxLayout()

        result_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )

        result_layout.setSpacing(
            12
        )

        result_card.setLayout(
            result_layout
        )

        result_title = QLabel(
            "DETECTION RESULT"
        )

        result_title.setStyleSheet("""
            QLabel {
                color: #6EA8FE;
                font-size: 13px;
                font-weight: bold;
                letter-spacing: 1px;
            }
        """)

        result_layout.addWidget(
            result_title
        )

        self.result_label = QLabel(
            "No scan performed."
        )

        self.result_label.setAlignment(
            Qt.AlignCenter
        )

        self.result_label.setMinimumHeight(
            80
        )

        self.result_label.setStyleSheet("""
            QLabel {
                background-color: #11161F;
                color: #AAB2C0;
                border-radius: 10px;
                padding: 15px;
                font-size: 18px;
                font-weight: bold;
            }
        """)

        result_layout.addWidget(
            self.result_label
        )

        main_layout.addWidget(
            result_card
        )

        # DETECTED TOOLS CARD
        tools_card = QFrame()

        tools_card.setStyleSheet("""
            QFrame {
                background-color: #181E28;
                border: 1px solid #293241;
                border-radius: 14px;
            }
        """)

        tools_layout = QVBoxLayout()

        tools_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )

        tools_layout.setSpacing(
            10
        )

        tools_card.setLayout(
            tools_layout
        )

        tools_title = QLabel(
            "DETECTED APPLICATIONS"
        )

        tools_title.setStyleSheet("""
            QLabel {
                color: #9B8AFB;
                font-size: 13px;
                font-weight: bold;
                letter-spacing: 1px;
            }
        """)

        tools_layout.addWidget(
            tools_title
        )

        self.detected_list = QListWidget()

        self.detected_list.setMinimumHeight(
            180
        )

        self.detected_list.setStyleSheet("""
            QListWidget {
                background-color: #11161F;
                color: #E8ECF3;
                border: 1px solid #303949;
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
            }

            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #252C38;
            }
        """)

        tools_layout.addWidget(
            self.detected_list
        )

        main_layout.addWidget(
            tools_card
        )

        # BUTTONS
        button_layout = QHBoxLayout()

        button_layout.setSpacing(
            12
        )

        self.scan_button = QPushButton(
            "🔍  Scan Now"
        )

        self.clear_button = QPushButton(
            "↻  Clear Results"
        )

        self.scan_button.clicked.connect(
            self.run_scan
        )

        self.clear_button.clicked.connect(
            self.clear_results
        )

        button_style = """
            QPushButton {
                background-color: #202938;
                color: #E8ECF3;
                border: 1px solid #374255;
                border-radius: 9px;
                padding: 12px 18px;
                font-size: 13px;
                font-weight: 600;
            }

            QPushButton:hover {
                background-color: #2A3548;
                border: 1px solid #6EA8FE;
            }

            QPushButton:pressed {
                background-color: #151B24;
            }
        """

        self.scan_button.setStyleSheet(
            button_style
        )

        self.clear_button.setStyleSheet(
            button_style
        )

        button_layout.addWidget(
            self.scan_button
        )

        button_layout.addWidget(
            self.clear_button
        )

        main_layout.addLayout(
            button_layout
        )

        # FOOTER
        footer = QLabel(
            "AI Assistant Detection System  •  Phase 3"
        )

        footer.setAlignment(
            Qt.AlignCenter
        )

        footer.setStyleSheet("""
            QLabel {
                color: #667085;
                font-size: 11px;
                padding-top: 4px;
            }
        """)

        main_layout.addWidget(
            footer
        )

    def run_scan(self):

        self.status_label.setText(
            "● SCANNING"
        )

        self.status_label.setStyleSheet("""
            QLabel {
                background-color: #172B3A;
                color: #6EA8FE;
                border: 1px solid #285477;
                border-radius: 18px;
                padding: 8px 16px;
                font-size: 12px;
                font-weight: bold;
            }
        """)

        QApplication.processEvents()

        results = self.detector.detect()

        self.detected_list.clear()

        if results:

            self.result_label.setText(
                "⚠  AI ASSISTANT DETECTED"
            )

            self.result_label.setStyleSheet("""
                QLabel {
                    background-color: #3A2020;
                    color: #FF8A8A;
                    border: 1px solid #6B3030;
                    border-radius: 10px;
                    padding: 15px;
                    font-size: 18px;
                    font-weight: bold;
                }
            """)

            self.status_label.setText(
                "● DETECTED"
            )

            self.status_label.setStyleSheet("""
                QLabel {
                    background-color: #3A2020;
                    color: #FF8A8A;
                    border: 1px solid #6B3030;
                    border-radius: 18px;
                    padding: 8px 16px;
                    font-size: 12px;
                    font-weight: bold;
                }
            """)

            for item in results:

                self.detected_list.addItem(
                    f"⚠  {item['name']}    "
                    f"(PID: {item['pid']})"
                )

            QMessageBox.warning(
                self,
                "AI Assistant Detected",
                "A known AI assistant process "
                "was detected on this computer."
            )

        else:

            self.result_label.setText(
                "✓  NO KNOWN AI ASSISTANT DETECTED"
            )

            self.result_label.setStyleSheet("""
                QLabel {
                    background-color: #123524;
                    color: #7CFFB2;
                    border: 1px solid #2E8B57;
                    border-radius: 10px;
                    padding: 15px;
                    font-size: 18px;
                    font-weight: bold;
                }
            """)

            self.status_label.setText(
                "● CLEAR"
            )

            self.status_label.setStyleSheet("""
                QLabel {
                    background-color: #123524;
                    color: #7CFFB2;
                    border: 1px solid #2E8B57;
                    border-radius: 18px;
                    padding: 8px 16px;
                    font-size: 12px;
                    font-weight: bold;
                }
            """)

            self.detected_list.addItem(
                "✓ No configured AI assistant "
                "processes detected."
            )

    def clear_results(self):

        self.detected_list.clear()

        self.result_label.setText(
            "No scan performed."
        )

        self.result_label.setStyleSheet("""
            QLabel {
                background-color: #11161F;
                color: #AAB2C0;
                border-radius: 10px;
                padding: 15px;
                font-size: 18px;
                font-weight: bold;
            }
        """)

        self.status_label.setText(
            "● READY"
        )

        self.status_label.setStyleSheet("""
            QLabel {
                background-color: #202733;
                color: #71D79A;
                border: 1px solid #334052;
                border-radius: 18px;
                padding: 8px 16px;
                font-size: 12px;
                font-weight: bold;
            }
        """)


def run_detector_app():

    app = QApplication(
        sys.argv
    )

    window = DetectionWindow()

    window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":

    run_detector_app()