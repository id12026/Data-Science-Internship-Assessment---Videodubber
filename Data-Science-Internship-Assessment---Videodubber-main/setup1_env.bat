@echo off
REM Check if Python is installed
where python
if %errorlevel% neq 0 (
    echo Python is not installed or not in the PATH.
    pause
    exit /b
)

REM Create a virtual environment
python -m venv myenv

REM Check if the virtual environment was created
if not exist "myenv\Scripts\activate" (
    echo Failed to create virtual environment.
    pause
    exit /b
)

REM Activate the virtual environment
call myenv\Scripts\activate

REM Downgrade NumPy to a compatible version
python -m pip install numpy<2

REM Install specific versions of dependencies
python -m pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 tensorflow==2.18.0 tensorboard>=2.18,<2.19 gfpgan==1.3.8 basicsr>=1.4.2

REM Deactivate the virtual environment
call myenv\Scripts\deactivate.bat

echo Setup complete!
pause