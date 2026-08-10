# MeetMind AI & MeetGuard AI

## AI Meeting Assistant and Detection System

This project is a three-phase desktop AI system developed as an academic project.

---

## MeetMind AI

### Real-Time AI Meeting Assistant

MeetMind AI is a desktop application that listens to spoken questions during online meetings, converts speech to text, sends the question to an AI language model, and displays the generated answer in real time.

### Features

- Voice-based question input
- Keyboard question input
- Speech-to-text
- AI-powered answer generation
- Real-time answer display
- Interactive desktop GUI
- Privacy mode

---

## MeetGuard AI

### AI Meeting Assistant Detection & Monitoring

MeetGuard AI is a separate desktop application designed to monitor running processes and identify configured AI assistant applications.

### Features

- Process monitoring
- Known AI-tool detection
- Detection status
- Application list
- Scan Now
- Clear Results
- Visual warning system

---

# Project Phases

## Phase 1
Real-Time AI Meeting Assistant

## Phase 2
Privacy During Screen Sharing

## Phase 3
AI Assistant Detection Tool

---

# Technologies

- Python
- PySide6
- Speech-to-Text
- Large Language Model
- Groq API
- psutil
- Windows process APIs

---

# Project Structure

phase1/
    AI Meeting Assistant

phase2/
    Privacy functionality

phase3/
    AI Assistant Detection

docs/
    Project documentation

tests/
    Testing files

---

# How to Run

Activate the virtual environment:

    .\venv\Scripts\Activate.ps1

Run MeetMind AI:

    python phase1\main.py

Run MeetGuard AI:

    python phase3\detector_ui.py

---

# Academic Project

This project demonstrates both AI assistance and AI-assistance detection from two different perspectives.