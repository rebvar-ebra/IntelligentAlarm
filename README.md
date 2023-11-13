# Intelligent Alarm

## Overview
The Intelligent Alarm is an innovative system combining a computer and a web camera to monitor and detect when a person wakes up. It's designed to be a smart and responsive way to start your day, using Python and image processing technologies.

## System Requirements
- **Computer**: Runs the Intelligent Alarm application.
- **Web Camera**: Must be capable of viewing a larger area than the sleeping area for accurate motion detection.

## Setup and Installation
1. **Camera Installation**: Position the webcam to oversee the entire sleeping area. It should capture a broader view than just the bed for precise motion detection.
2. **Define Sleeping Area**: Use the control program to specify the sleeping area (e.g., bed rectangle).
3. **Set Wake-Up Time**: Enter the desired wake-up time into the system.

## Operation
- **Alarm Activation**: The alarm activates at the preset wake-up time, alerting the user.
- **Wake Detection**: The system detects when the user has left the sleeping area and does not return, indicating wakefulness.
- **Single Person Tracking**: The system is designed to track the awakening of only the first person who wakes up in the sleeping area.

## Implementation Details
- **Programming Language**: Implemented using Python.
- **Key Libraries**: Utilizes OpenCV for image processing to analyze the camera feed.
- **Alarm Mechanism**: Python scripts manage the alarm functionality, ensuring a reliable wake-up experience.

## Getting Started
To get started with the Intelligent Alarm:
1. Clone the repository: `git clone https://github.com/rebvar-ebra/IntelligentAlarm.git`
2. Install the required Python packages: `pip install -r requirements.txt`
3. Run the application: `python main.py`


