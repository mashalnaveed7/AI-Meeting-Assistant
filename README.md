# AI Meeting Assistant & Detection System

## Project Overview

This project is a desktop-based AI Meeting Assistant designed to help users during online meetings by converting spoken questions into text, generating relevant AI-based answers, and displaying those answers through a desktop interface.

The project consists of three phases:

### Phase 1 - AI Meeting Assistant
- Capture spoken questions
- Convert speech to text
- Analyze questions using an LLM
- Display relevant answers

### Phase 2 - Privacy During Screen Sharing
- Provide a privacy mode
- Hide sensitive AI content when privacy mode is activated
- Provide a clear privacy status indicator

### Phase 3 - AI Assistant Detection Tool
- Scan running Windows processes
- Identify applications from a configurable list of known AI assistant processes
- Display detection results to the user

## Technology Stack

- Python
- PySide6
- Speech-to-Text
- Large Language Model
- Windows APIs
- psutil
- GitHub
## Current Progress

### Day 1
- Project structure created
- PySide6 desktop GUI created
- GitHub repository configured

### Day 2
- Microphone integration completed
- Speech-to-text completed
- Spoken questions displayed in GUI

### Day 3
- Groq LLM integration completed
- AI answer generation completed
- AI answers displayed in GUI



- ### Day 4

- Implemented Phase 2 privacy mode.
- Added Windows screen-capture exclusion using SetWindowDisplayAffinity.
- Added Privacy Mode ON/OFF control.
- Redesigned the desktop GUI.
- Added interactive buttons and status indicators.
- Improved question and answer layout.
- Added professional dark theme.
### Day 5

- Implemented Phase 3 AI assistant detection.
- Added Windows process scanning using psutil.
- Added configurable known AI assistant list.
- Added process detection logic.
- Added detection warning system.
- Created separate Phase 3 desktop GUI.
- Added Scan Now and Clear Results controls.
- Added safe mock AI assistant process for testing.
- Tested both detection and clear states.

### Upcoming

### Day 6

- Full system testing
- Bug fixing
- Phase integration
- Performance improvements

### Day 7

- Final documentation
- Final GUI polish
- Demonstration preparation
- Final GitHub update

