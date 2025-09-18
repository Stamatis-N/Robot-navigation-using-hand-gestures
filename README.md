robot-gesture-navigation/
│── main.py
│── hands_tracking.py
│── robot.py
│── requirements.txt
│── README.md
│── Report.pdf

# 🤖 Robot Navigation Using Hand Gestures

## 📌 Description
This project implements a robot that moves in space using specific hand gestures detected by the computer’s camera.  
- **Right hand** is recognized when the **palm is facing the camera**.  
- **Left hand** is recognized when the **back of the hand faces the camera**.  


## ⚙️ Requirements
- Python 3.12.11
- All other dependencies are listed in `requirements.txt`


### 1. Download the project
Download the project files to your computer.

### 2. Create a Conda environment (recommended)
conda create --name robot_env python=3.12.11
conda activate robot_env

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the script
python main.py

### 5. Aftermath
After the program is completed, it will automatically save a .png file with the robot's route at the same folder as the project.

## Important note
The script requires to open your computer's camera. It will automatically open the default camera.
Ensure that your camera is working properly before running the program.

## Troubleshooting
If you have problem running the program type in the terminal:
conda install -c conda-forge ghostscript

If dependencies fail to install, update pip:
python -m pip install --upgrade pip