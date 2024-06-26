# HexTech TurnTable
###  Description: Drone Antenna Tracking System with MQTT Communication

The turntable features a modern aesthetic, utilizing a single stepper motor and a microswitch to smoothly rotate the table and provide drone antenna tracking. The turntable dynamically adjusts its orientation based on the drone's GPS coordinates to maintain optimal communication. A graphical user interface guides users to set a zero/north reference point by entering the turntable's coordinates. Users can then input the drone's GPS coordinates to enable automatic tracking. The system utilizes the paho.mqtt.client library to manage MQTT operations, including connecting to the broker, publishing messages, and handling incoming messages. This ensures efficient communication between the turntable and the control system.

### Possible Challenges:
- GPS acuracy and delay: Minimizing the delay between receiving GPS coordinates and adjusting the turntable to ensure real-time tracking
- Compatability with various antennas
