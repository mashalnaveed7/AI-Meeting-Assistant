# System Architecture

## Project

AI Meeting Assistant & Detection System

## Phase 1

The AI Meeting Assistant follows this workflow:

Microphone
→ Speech-to-Text
→ Question Text
→ Large Language Model
→ AI Answer
→ Desktop GUI

## Phase 2

The application provides a privacy mode that changes the visibility of sensitive AI-generated content.

## Phase 3

A separate detection application scans running Windows processes and compares them against a configurable list of known AI assistant processes.

## Main Technologies

- Python
- PySide6
- Speech-to-Text
- Large Language Model
- psutil
- Windows Desktop Environment