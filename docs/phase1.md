# Phase 1 - AI Meeting Assistant

## Day 3 Progress

The Large Language Model integration has been completed.

## Current Workflow

Microphone
→ Speech-to-Text
→ Question
→ Groq LLM
→ AI Answer
→ PySide6 GUI

## Technologies Used

- Python
- PySide6
- SpeechRecognition
- PyAudio
- Groq API
- Llama 3.1
- python-dotenv

## Current Functionality

The application can:

1. Listen to the user's microphone.
2. Convert spoken questions into text.
3. Display the question in the GUI.
4. Send the question to an LLM.
5. Generate an AI-based answer.
6. Display the answer in the GUI.

## Security

The Groq API key is stored in a local `.env` file and is excluded from GitHub using `.gitignore`.

## Current Limitation

The current prototype processes one spoken question at a time.

Continuous meeting conversation handling will be improved in later development.

## Status

Speech-to-text: Completed

LLM integration: Completed

AI answer display: Completed

Continuous meeting processing: Planned