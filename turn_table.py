import time
import os
import paho.mqtt.client as mqtt

STEPS_PER_REVOLUTION = 2393

USERNAME = "hextech-andrea"
PASSWORD = "andrea"
commands = "hextech/hextech-andrea/commands"
topic = "hextech/hextech-andrea/status"

unacked_publish = set()
POSITION_FILE = "position.txt"


def main():
    mqttc = setup_mqtt()
    initialize_position()
    steps = read_steps()
    if steps is not None:
        move_and_update_position(mqttc, steps)

    # Stop the loop and disconnect
    mqttc.disconnect()
    mqttc.loop_stop()


def initialize_position():
    if not os.path.exists(POSITION_FILE):
        # Zero the turntable and set the initial position to 0
        print("Zeroing the turntable...")
        zero_turntable()
        with open(POSITION_FILE, "w") as file:
            file.write("0")
        print("Turntable zeroed and initial position set to 0.")


def zero_turntable():
    mqttc = setup_mqtt()
    home_payload = "zeroX"
    publish_and_wait(mqttc, home_payload)
    mqttc.disconnect()
    mqttc.loop_stop()


def read_steps():
    try:
        with open("steps.txt", "r") as file:
            steps = int(file.read().strip())
            print(f"Read steps: {steps}")
            return steps
    except FileNotFoundError:
        print("Steps file not found.")
        return None


def on_publish(client, userdata, mid, reason_code, properties):
    # removes the message ID from the set of unacknowledged messages
    userdata.remove(mid)
    print(f"Published message ID: {mid}")


def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe(topic)


def on_message(client, userdata, msg):
    print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")


def setup_mqtt():
    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    # Assign callbacks
    mqttc.on_publish = on_publish
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message

    # Set user data (this stores unacknowledged message ids)
    mqttc.user_data_set(unacked_publish)

    # Set username and password
    mqttc.username_pw_set(username=USERNAME, password=PASSWORD)

    # Connect to the MQTT server
    mqttc.connect("mqtt.hextronics.cloud", 1883)

    # Start network loop
    mqttc.loop_start()

    return mqttc


def move_and_update_position(mqttc, steps):
    current_position = read_current_position()
    target_position = (current_position + steps) % STEPS_PER_REVOLUTION
    relative_steps = target_position - current_position

    # Command to move the required number of steps
    steps_payload = f"stepper.00_speed_400|stepper.00_move_{relative_steps}_1"
    publish_and_wait(mqttc, steps_payload)

    # Update the position file
    with open(POSITION_FILE, "w") as file:
        file.write(str(target_position))


def publish_and_wait(mqttc, payload):
    msg_info = mqttc.publish(commands, payload, 0, False)
    unacked_publish.add(msg_info.mid)

    # Wait for the message to be acknowledged
    while len(unacked_publish):
        time.sleep(0.1)

    # Safe way to wait for publish
    msg_info.wait_for_publish()


def read_current_position():
    try:
        with open(POSITION_FILE, "r") as file:
            position = int(file.read().strip())
            return position
    except FileNotFoundError:
        print("Position file not found. Initializing to 0.")
        return 0


if __name__ == "__main__":
    main()
