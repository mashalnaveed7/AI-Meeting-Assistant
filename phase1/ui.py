import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QFrame
)


class MeetingAssistantWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Meeting Assistant")
        self.setMinimumSize(800, 600)

        self.create_ui()

    def create_ui(self):

        # Main central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(15)

        central_widget.setLayout(main_layout)

        # Title
        title = QLabel("AI MEETING ASSISTANT")
        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            QLabel {
                font-size: 28px;
                font-weight: bold;
                padding: 15px;
            }
        """)

        main_layout.addWidget(title)

        # Status
        self.status_label = QLabel("Status: Ready")

        self.status_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                padding: 10px;
            }
        """)

        main_layout.addWidget(self.status_label)

        # Question heading
        question_heading = QLabel("Question")

        question_heading.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
            }
        """)

        main_layout.addWidget(question_heading)

        # Question text box
        self.question_box = QTextEdit()
        self.question_box.setPlaceholderText(
            "The spoken meeting question will appear here..."
        )

        self.question_box.setReadOnly(True)

        self.question_box.setMinimumHeight(100)

        main_layout.addWidget(self.question_box)

        # Answer heading
        answer_heading = QLabel("AI Answer")

        answer_heading.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
            }
        """)

        main_layout.addWidget(answer_heading)

        # Answer text box
        self.answer_box = QTextEdit()
        self.answer_box.setPlaceholderText(
            "The AI-generated answer will appear here..."
        )

        self.answer_box.setReadOnly(True)

        self.answer_box.setMinimumHeight(150)

        main_layout.addWidget(self.answer_box)

        # Buttons
        button_layout = QHBoxLayout()

        self.start_button = QPushButton("Start Assistant")
        self.stop_button = QPushButton("Stop Assistant")
        self.clear_button = QPushButton("Clear")

        self.start_button.clicked.connect(self.start_assistant)
        self.stop_button.clicked.connect(self.stop_assistant)
        self.clear_button.clicked.connect(self.clear_content)

        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.clear_button)

        main_layout.addLayout(button_layout)

        # Privacy status
        self.privacy_label = QLabel("Privacy Mode: OFF")
        self.privacy_label.setAlignment(Qt.AlignCenter)

        self.privacy_label.setStyleSheet("""
            QLabel {
                font-size: 15px;
                font-weight: bold;
                padding: 10px;
            }
        """)

        main_layout.addWidget(self.privacy_label)

        # Footer
        footer = QLabel(
            "AI Meeting Assistant - Three Phase Academic Project"
        )

        footer.setAlignment(Qt.AlignCenter)

        footer.setStyleSheet("""
            QLabel {
                font-size: 12px;
                padding: 10px;
            }
        """)

        main_layout.addWidget(footer)

    def start_assistant(self):

        self.status_label.setText("Status: Assistant Running")

        self.question_box.setPlainText(
            "Waiting for a meeting question..."
        )

        self.answer_box.setPlainText(
            "AI answer will appear here."
        )

    def stop_assistant(self):

        self.status_label.setText("Status: Assistant Stopped")

    def clear_content(self):

        self.question_box.clear()
        self.answer_box.clear()

        self.status_label.setText("Status: Ready")


def run_app():

    app = QApplication(sys.argv)

    window = MeetingAssistantWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    run_app()