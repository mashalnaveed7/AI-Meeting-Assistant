import sys

from PySide6.QtCore import Qt, QThread, Signal
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

from ai_service import AIService
from speech_to_text import SpeechToText

from phase2.privacy_mode import PrivacyMode
from phase2.privacy_ui import PrivacyStatusWidget


class SpeechWorker(QThread):

    transcription_ready = Signal(str)
    answer_ready = Signal(str)
    listening_status = Signal(str)

    def __init__(self):

        super().__init__()

        self.speech_to_text = SpeechToText()
        self.ai_service = AIService()

    def run(self):

        self.listening_status.emit(
            "LISTENING"
        )

        text = self.speech_to_text.listen()

        if not text:

            self.listening_status.emit(
                "NO QUESTION DETECTED"
            )

            return

        self.transcription_ready.emit(text)

        self.listening_status.emit(
            "GENERATING ANSWER"
        )

        answer = self.ai_service.get_answer(text)

        self.answer_ready.emit(answer)

        self.listening_status.emit(
            "READY"
        )


class MeetingAssistantWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "MeetMind AI"
        )

        self.setMinimumSize(
            950,
            700
        )

        self.speech_worker = None

        self.privacy_mode = PrivacyMode(self)

        self.create_ui()

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

        main_layout.setSpacing(18)

        central_widget.setLayout(
            main_layout
        )

        # =========================================
        # HEADER
        # =========================================

        header_layout = QHBoxLayout()

        title_layout = QVBoxLayout()

        title = QLabel(
            "MeetMind AI"
        )

        title.setStyleSheet("""
            QLabel {
                color: #F4F7FB;
                font-size: 27px;
                font-weight: 700;
            }
        """)

        subtitle = QLabel(
            "Real-Time AI Meeting Assistant"
        )

        subtitle.setStyleSheet("""
            QLabel {
                color: #8E99AA;
                font-size: 13px;
                margin-top: 2px;
            }
        """)

        title_layout.addWidget(title)
        title_layout.addWidget(subtitle)

        header_layout.addLayout(
            title_layout
        )

        header_layout.addStretch()

        # Status indicator
        self.status_label = QLabel(
            "●  READY"
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

        # =========================================
        # QUESTION CARD
        # =========================================

        question_card = QFrame()

        question_card.setStyleSheet("""
            QFrame {
                background-color: #181E28;
                border: 1px solid #293241;
                border-radius: 14px;
            }
        """)

        question_layout = QVBoxLayout()

        question_layout.setContentsMargins(
            20,
            18,
            20,
            18
        )

        question_layout.setSpacing(10)

        question_card.setLayout(
            question_layout
        )

        question_title = QLabel(
            "QUESTION"
        )

        question_title.setStyleSheet("""
            QLabel {
                color: #6EA8FE;
                font-size: 13px;
                font-weight: bold;
                letter-spacing: 1px;
            }
        """)

        question_layout.addWidget(
            question_title
        )

        self.question_box = QTextEdit()

        self.question_box.setPlaceholderText(
    "Speak your question or type your question here..."
)

        self.question_box.setMinimumHeight(
    100
)

        self.question_box.setStyleSheet("""
            QTextEdit {
                background-color: #11161F;
                color: #E8ECF3;
                border: 1px solid #303949;
                border-radius: 10px;
                padding: 12px;
                font-size: 14px;
            }

            QTextEdit:focus {
                border: 1px solid #6EA8FE;
            }
        """)

        question_layout.addWidget(
            self.question_box
        )

        # Ask AI button - placed directly below the question box
        self.ask_button = QPushButton(
            "🤖  Ask AI"
        )

        self.ask_button.setMinimumHeight(
            42
        )

        self.ask_button.setStyleSheet("""
            QPushButton {
                background-color: #6C5CE7;
                color: white;
                border: 1px solid #8B7CF6;
                border-radius: 9px;
                padding: 10px 18px;
                font-size: 13px;
                font-weight: 700;
            }

            QPushButton:hover {
                background-color: #7B6CF0;
                border: 1px solid #A69BFF;
            }

            QPushButton:pressed {
                background-color: #5748C7;
            }
        """)

        self.ask_button.clicked.connect(
            self.ask_ai
        )

        question_layout.addWidget(
            self.ask_button
        )

        main_layout.addWidget(
            question_card
        )

        # =========================================
        # ANSWER CARD
        # =========================================

        answer_card = QFrame()

        answer_card.setStyleSheet("""
            QFrame {
                background-color: #181E28;
                border: 1px solid #293241;
                border-radius: 14px;
            }
        """)

        answer_layout = QVBoxLayout()

        answer_layout.setContentsMargins(
            20,
            18,
            20,
            18
        )

        answer_layout.setSpacing(10)

        answer_card.setLayout(
            answer_layout
        )

        answer_title = QLabel(
            "AI ANSWER"
        )

        answer_title.setStyleSheet("""
            QLabel {
                color: #9B8AFB;
                font-size: 13px;
                font-weight: bold;
                letter-spacing: 1px;
            }
        """)

        answer_layout.addWidget(
            answer_title
        )

        self.answer_box = QTextEdit()

        self.answer_box.setPlaceholderText(
            "The AI-generated answer will appear here..."
        )

        self.answer_box.setReadOnly(
            True
        )

        self.answer_box.setMinimumHeight(
            190
        )

        self.answer_box.setStyleSheet("""
            QTextEdit {
                background-color: #11161F;
                color: #E8ECF3;
                border: 1px solid #303949;
                border-radius: 10px;
                padding: 12px;
                font-size: 14px;
            }

            QTextEdit:focus {
                border: 1px solid #9B8AFB;
            }
        """)

        answer_layout.addWidget(
            self.answer_box
        )

        main_layout.addWidget(
            answer_card
        )

        # =========================================
        # BUTTONS
        # =========================================

        button_layout = QHBoxLayout()

        button_layout.setSpacing(
            12
        )

        self.start_button = QPushButton(
            "🎤  Start Listening"
        )

        self.stop_button = QPushButton(
            "■  Stop"
        )

        self.clear_button = QPushButton(
            "↻  Clear"
        )
        self.privacy_button = QPushButton(
            "🔒  Privacy Mode"
        )

        self.start_button.clicked.connect(
            self.start_assistant
        )

        self.stop_button.clicked.connect(
            self.stop_assistant
        )

        self.clear_button.clicked.connect(
            self.clear_content
        )
        self.privacy_button.clicked.connect(
            self.toggle_privacy
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

        self.start_button.setStyleSheet(
            button_style
        )

        self.stop_button.setStyleSheet(
            button_style
        )

        self.clear_button.setStyleSheet(
            button_style
        )
        self.ask_button.setStyleSheet(
            button_style
        )
        self.privacy_button.setStyleSheet(
            button_style
        )

        button_layout.addWidget(
            self.start_button
        )

        button_layout.addWidget(
            self.stop_button
        )

        button_layout.addWidget(
            self.clear_button
        )
        button_layout.addWidget(
            self.privacy_button
        )

        main_layout.addLayout(
            button_layout
        )

        # =========================================
        # PRIVACY STATUS
        # =========================================

        self.privacy_label = PrivacyStatusWidget()

        main_layout.addWidget(
            self.privacy_label
        )

        # =========================================
        # FOOTER
        # =========================================

        footer = QLabel(
            "MeetMind AI • Real-Time AI Meeting Assistant"
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

    # =============================================
    # START ASSISTANT
    # =============================================

    def start_assistant(self):

        self.status_label.setText(
            "●  STARTING"
        )

        self.status_label.setStyleSheet("""
            QLabel {
                background-color: #202733;
                color: #FFD166;
                border: 1px solid #334052;
                border-radius: 18px;
                padding: 8px 16px;
                font-size: 12px;
                font-weight: bold;
            }
        """)

        self.speech_worker = SpeechWorker()

        self.speech_worker.transcription_ready.connect(
            self.update_question
        )

        self.speech_worker.answer_ready.connect(
            self.update_answer
        )

        self.speech_worker.listening_status.connect(
            self.update_status
        )

        self.speech_worker.start()

    # =============================================
    # STOP ASSISTANT
    # =============================================

    def stop_assistant(self):

        self.status_label.setText(
            "●  STOPPED"
        )

        self.status_label.setStyleSheet("""
            QLabel {
                background-color: #202733;
                color: #FF7B7B;
                border: 1px solid #334052;
                border-radius: 18px;
                padding: 8px 16px;
                font-size: 12px;
                font-weight: bold;
            }
        """)

        if self.speech_worker is not None:

            self.speech_worker.quit()

            self.speech_worker.wait()

            self.speech_worker = None

    # =============================================
    # UPDATE QUESTION
    # =============================================

    def update_question(self, text):

        self.question_box.setPlainText(
            text
        )

    # =============================================
    # UPDATE ANSWER
    # =============================================

    def update_answer(self, answer):

        self.answer_box.setPlainText(
            answer
        )

    # =============================================
    # UPDATE STATUS
    # =============================================

    def update_status(self, status):

        if status == "LISTENING":

            self.status_label.setText(
                "●  LISTENING"
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

        elif status == "GENERATING ANSWER":

            self.status_label.setText(
                "●  THINKING"
            )

            self.status_label.setStyleSheet("""
                QLabel {
                    background-color: #29243B;
                    color: #B8A7FF;
                    border: 1px solid #4B3E70;
                    border-radius: 18px;
                    padding: 8px 16px;
                    font-size: 12px;
                    font-weight: bold;
                }
            """)

        elif status == "NO QUESTION DETECTED":

            self.status_label.setText(
                "●  NO QUESTION"
            )

            self.status_label.setStyleSheet("""
                QLabel {
                    background-color: #382D1B;
                    color: #FFD166;
                    border: 1px solid #66501E;
                    border-radius: 18px;
                    padding: 8px 16px;
                    font-size: 12px;
                    font-weight: bold;
                }
            """)

        else:

            self.status_label.setText(
                "●  READY"
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

    def keyPressEvent(self, event):

        if (
            event.key() == Qt.Key_Return
            and event.modifiers() & Qt.ControlModifier
        ):
            self.ask_ai()
            event.accept()
            return

        super().keyPressEvent(event)

    # =============================================
    # ASK AI
    # =============================================

    def ask_ai(self):

        question = self.question_box.toPlainText().strip()

        if not question:

            self.status_label.setText(
                "●  PLEASE ENTER A QUESTION"
            )

            self.status_label.setStyleSheet("""
                QLabel {
                    background-color: #382D1B;
                    color: #FFD166;
                    border: 1px solid #66501E;
                    border-radius: 18px;
                    padding: 8px 16px;
                    font-size: 12px;
                    font-weight: bold;
                }
            """)

            self.answer_box.setPlainText(
                "Please enter a question first."
            )

            return

        self.status_label.setText(
            "●  GENERATING ANSWER"
        )

        self.status_label.setStyleSheet("""
            QLabel {
                background-color: #29243B;
                color: #B8A7FF;
                border: 1px solid #4B3E70;
                border-radius: 18px;
                padding: 8px 16px;
                font-size: 12px;
                font-weight: bold;
            }
        """)

        try:

            ai_service = AIService()

            answer = ai_service.get_answer(
                question
            )

            if answer:

                self.answer_box.setPlainText(
                    str(answer)
                )

                self.status_label.setText(
                    "●  READY"
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

            else:

                self.answer_box.setPlainText(
                    "No answer was returned by the AI service."
                )

                self.status_label.setText(
                    "●  NO ANSWER"
                )

        except Exception as error:

            print("Keyboard AI error:")
            print(error)

            self.answer_box.setPlainText(
                "Sorry, I could not generate an answer.\n\n"
                + str(error)
            )

            self.status_label.setText(
                "●  AI ERROR"
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

    # =============================================
    # PRIVACY MODE
    # =============================================

    def toggle_privacy(self):

        success = self.privacy_mode.toggle()

        if success:

            if self.privacy_mode.is_enabled():

                self.privacy_label.set_privacy_on()

                self.privacy_button.setText(
                    "🔓  Disable Privacy"
                )

            else:

                self.privacy_label.set_privacy_off()

                self.privacy_button.setText(
                    "🔒  Privacy Mode"
                )

        else:

            self.privacy_label.setText(
                "⚠  Privacy Mode could not be enabled"
            )

            self.privacy_label.setStyleSheet("""
                QLabel {
                    background-color: #3A2020;
                    color: #FF8A8A;
                    border: 1px solid #6B3030;
                    border-radius: 10px;
                    padding: 8px 16px;
                    font-size: 13px;
                    font-weight: bold;
                }
            """)

    # =============================================
    # CLEAR
    # =============================================

    def clear_content(self):

        self.question_box.clear()

        self.answer_box.clear()

        self.status_label.setText(
            "●  READY"
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


def run_app():

    app = QApplication(sys.argv)

    window = MeetingAssistantWindow()

    window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":

    run_app()