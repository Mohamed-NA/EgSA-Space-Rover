# Rover Robot Prototype

A six-wheeled rover robot designed for navigating rough terrains using a Rocker-Bogie suspension system. Built to overcome obstacles like stairs and varied geographic surfaces with minimal human intervention.

## Overview

This research prototype focuses on autonomous mobility and robust terrain traversal. The suspension and drive system allow the rover to climb stairs, navigate uneven surfaces, and maintain balance in harsh environments.

## Technologies Used

- **Hardware:**
  - Raspberry Pi (Raspberry Pi OS)
  - LiDAR sensor
  - Camera module
  - DC motors with motor drivers

- **Software:**
  - Python
  - Custom Simple Serial Protocol (SSP)
  - Linux-based system control

## My Contributions

- Developed control logic in **Python** to operate:
  - Motors for movement
  - LiDAR for environment sensing
  - Camera for vision input
- Built a **manual implementation of SSP (Simple Serial Protocol)** to enable reliable communication between hardware modules.

## Project Structure
```
rover-robot/
├── control/
│ ├── motor_control.py
│ ├── lidar_handler.py
│ └── camera_stream.py
├── protocols/
│ └── ssp.py
├── main.py
└── README.md
```
## Features

- Rocker-Bogie mechanical system for obstacle navigation.
- Modular architecture for motor, sensor, and camera control.
- Custom communication protocol between Raspberry Pi and subsystems.
- Lightweight and efficient design for real-time performance.

## Skills Demonstrated

`Python` • `Embedded Systems` • `Robotics` • `Linux` • `Raspberry Pi` • `Sensor Integration` • `Protocol Design`

## Connect

Feel free to reach out if you want to collaborate or learn more about this project!

**Mohamed Nasser**
[LinkedIn](https://www.linkedin.com/in/mohamed-nasser-ahmed)
