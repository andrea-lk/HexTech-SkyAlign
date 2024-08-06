# HexTech SkyAlign

The SkyAlign is a turntable that dynamically tracks a drone's location by adjusting its orientation based on the drone's GPS coordinates to maintain optimal communication.

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Possible Challenges](#possible-challenges)
- [Contributing](#contributing)
- [License](#license)

## Project Description

SkyAlign is designed to ensure optimal communication with drones by dynamically adjusting its orientation. Users can manually align the turntable to true north using a compass or GPS device. Once aligned, the initial orientation is stored for future reference. Upon startup, the turntable resets to the zero position to ensure accuracy. Users can input the drone's GPS coordinates into the GUI for automatic tracking. The system calculates the required bearing and step adjustments to orient the turntable towards the drone, ensuring continuous tracking accuracy.

## Features
- **True North Alignment**: Users can set the turntable to true north using a compass or GPS device.
- **Automatic Tracking**: Tracks a drone's location dynamically based on GPS coordinates.
- **Startup Calibration**: Resets to zero position at startup to ensure accuracy.
- **Infinite Tracking Adjustments**: Allows continuous updates to the drone's coordinates for tracking.
- **MQTT Integration**: Manages MQTT operations for communication and control.

## Installation
To set up this project locally, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/SkyAlign.git
   cd SkyAlign
2. **Install dependencies**: Ensure you have `tkinter` and `paho-mqtt` installed. You can install them using pip:
   ```sh
  pip install paho-mqtt


## Usage

1. **Running the GUI**:
   To run the graphical user interface, execute the following command:
   ```sh
   python GUI.py

2. Command-line Usage:
The turntable operates continuously to check for new step commands based on the drone's coordinates.

## Code Overview

### GUI.py

This file contains the code for the graphical user interface using `tkinter`.

* **Turntable Process**: Starts the turntable script in a separate process.
* **Input Boxes and Buttons**: Creates input fields for GPS coordinates and buttons for submission and clearing.
* **Submit Function**: Handles the input coordinates, writes them to a file, and runs the calculations script.
* **Clear Function**: Clears the input fields.

### calculations.py

This file calculates the bearing and steps required to orient the turntable towards the drone.

* **Read Coordinates**: Reads the GPS coordinates from a file.
* **Calculate Bearing**: Computes the bearing between the turntable and the drone.
* **Bearing to Steps**: Converts the bearing into the number of steps for the turntable.
* **Write Steps**: Writes the calculated steps to a file.

### turn_table.py

This file handles the turntable's movements based on the calculated steps and manages MQTT communication.

* **Reset to Zero**: Ensures the turntable is accurately set to the zero position at startup.
* **Read Steps**: Reads the steps from a file and moves the turntable accordingly.
* **MQTT Setup**: Initializes MQTT client and handles connection, publishing, and subscribing.
* **Move and Update Position**: Moves the turntable based on the required steps and updates the current position.


## Possible Challenges:
- Environmental factors, such as magnetic interference or poor GPS signal
- Stepper motor malfunctions or microswitch failures could disrupt the smooth rotation of the turntable
- Proper handling of MQTT operations

## Project Organization: 
- The src directory contains python. 
