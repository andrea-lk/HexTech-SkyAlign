# HexTech TurnTable
###  Description: 

This turntable dynamically tracks a drone's location by adjusting its orientation based on the drone's GPS coordinates to maintain optimal communication. To set the turntable to true north, users manually align it using a compass or GPS device. Once aligned, the initial true north orientation is set within the system and stored for future reference. Upon start up, the turntable resets to the 0 position. If the turntable is already at the zero position, the turntable will take 20 steps backwards and then return to the zero position to ensure the zero position it is in is accurate. Users may then input the drone's GPS coordinates into the GUI for automatic tracking an infinite amount of times. The program calculates the required bearing and step adjustments to orient the turntable towards the drone. After startup, if previous coordinates have already been entered and the turntable has moved to them, the program will calculate the steps based on the turntable's current position to adjust to any new coordinates entered subsequently. This ensures that the turntable continuously tracks the drone accurately by building off of the previous step number. It uses the paho.mqtt.client library to manage MQTT operations, including connecting to the broker and publishing messages.


## Possible Challenges:
- Environmental factors, such as magnetic interference or poor GPS signal
- Stepper motor malfunctions or microswitch failures could disrupt the smooth rotation of the turntable
- Proper handling of MQTT operations

## Project Organization: 
- The src directory contains python. 
