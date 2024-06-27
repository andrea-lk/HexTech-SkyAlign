# HexTech TurnTable
###  Description: Drone Tracking System with MQTT Communication

This turntable dynamically tracks a drone's location by adjusting its orientation based on the drone's GPS coordinates to maintain optimal communication. To set the turntable to true north, users manually align it using a compass or GPS device. Once aligned, the initial true north orientation is set within the system and stored for future reference. Users then input the drone's GPS coordinates into the graphical user interface for automatic tracking. The system calculates the required bearing and step adjustments to orient the turntable towards the drone. It uses the paho.mqtt.client library to manage MQTT operations, including connecting to the broker, publishing messages, and handling incoming messages.


## Possible Challenges:
- One potential challenge is ensuring accurate alignment of the turntable to true north. If users fail to orient the turntable correctly, the system may not track the drone accurately
- Environmental factors, such as magnetic interference or poor GPS signal
- Stepper motor malfunctions or microswitch failures could disrupt the smooth rotation of the turntable
- Proper handling of MQTT operations

## Project Organization: 
- The src directory contains python. 
