# HexTech TurnTable
###  Description: Drone Tracking System with MQTT Communication

This turntable dynamically tracks a drone's location,  adjusting its orientation based on the drone's GPS coordinates to maintain optimal communication. To set the turntable to true north, users manually align it using a compass or GPS device. Once aligned, users enter the true north orientation into the graphical user interface. Users can then input the drone's GPS coordinates for automatic tracking. The system uses the paho.mqtt.client library to manage MQTT operations, including connecting to the broker, publishing messages, and handling incoming messages. This ensures efficient communication between the turntable and the control system.


### Possible Challenges:
- One potential challenge is ensuring accurate alignment of the turntable to true north. If users fail to orient the turntable correctly, the system may not track the drone accurately
- Environmental factors, such as magnetic interference or poor GPS signal
- Stepper motor malfunctions or microswitch failures could disrupt the smooth rotation of the turntable
- Proper handling of MQTT operations
