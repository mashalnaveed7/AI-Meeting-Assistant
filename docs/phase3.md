# Phase 3 - AI Assistant Detection Tool

## Objective

Develop a separate desktop application that can detect known AI assistant applications running on a Windows computer.

## Technology

- Python
- PySide6
- psutil
- JSON
- Windows process enumeration

## How It Works

The detector scans currently running processes.

Each process is compared with a configurable list of known AI assistant process names stored in:

phase3/known_apps.json

## Detection Flow

Running Processes
        ↓
Process Name
        ↓
Compare with known_apps.json
        ↓
Detection Result
        ↓
Warning if a match is found

## Features

- Scan running processes
- Configurable known AI tool list
- Detection result
- Warning dialog
- Process ID display
- Professional desktop GUI
- Clear results button
- Manual scan button

## Testing

A mock AI assistant process was created for safe testing.

When the mock process is running:

AI Assistant Detected

When the mock process is stopped:

No Known AI Assistant Detected

## Important Limitation

This prototype detects applications based on configured process information.

It cannot guarantee detection of every possible AI assistant, renamed executable, browser-based service, or application using a different process architecture.

## Status

Phase 3 prototype completed.