@echo off
REM Create a virtual environment
python -m venv myenv

REM Activate the virtual environment
call myenv\Scripts\activate

REM Downgrade NumPy to a compatible version
python -m pip install numpy<2

REM Install the required dependencies
python -m pip install -r C:\Users\HEMANTH\Documents\musetalk\MuseTalk\requirements.txt

REM Deactivate the virtual environment
call myenv\Scripts\deactivate.bat

echo Setup complete!
pause