@echo off

py -m venv .pyarmy

:: Activate the virtual environment
call .pyarmy\Scripts\activate.bat

:: Install pygame
python -m pip install pygame

:: Confirmation message
echo Virtual environment setup complete!

:: Activate the virtual environment
./.pyarmy/scripts/activate
