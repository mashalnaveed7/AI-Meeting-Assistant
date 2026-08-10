import sys
from pathlib import Path

# Get the main project folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Add the main project folder to Python's import path
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Add phase1 folder so ui.py can find ai_service.py
PHASE1_FOLDER = Path(__file__).resolve().parent

if str(PHASE1_FOLDER) not in sys.path:
    sys.path.insert(0, str(PHASE1_FOLDER))

from ui import run_app


if __name__ == "__main__":
    run_app()