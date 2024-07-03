import math

STEPS_PER_REVOLUTION = 2393


def main():
    turntable_lat, turntable_long, drone_lat, drone_long = read_coordinates()
    if turntable_lat is not None:
        bearing = calculate_bearing(turntable_lat, turntable_long, drone_lat, drone_long)
        print(f"Calculated bearing: {bearing} degrees")
        steps = bearing_to_steps(bearing)
        print(f"Steps to turn: {steps} steps")
        write_steps(steps)


def read_coordinates():
    try:
        with open("coordinates.txt", "r") as file:
            data = file.read().strip().split(',')
            turntable_lat = float(data[0])
            turntable_long = float(data[1])
            drone_lat = float(data[2])
            drone_long = float(data[3])
            print(f"Read coordinates: Turntable Latitude = {turntable_lat}, Longitude = {turntable_long}")
            print(f"Drone Latitude = {drone_lat}, Longitude = {drone_long}")
            return turntable_lat, turntable_long, drone_lat, drone_long
    except FileNotFoundError:
        print("Coordinates file not found.")
        return None, None, None, None


def bearing_to_steps(bearing):
    steps = (bearing / 360) * STEPS_PER_REVOLUTION
    return int(steps)


def write_steps(steps):
    with open("steps.txt", "w") as file:
        file.write(str(steps))


def calculate_bearing(lat1, long1, lat2, long2):
    lat1 = math.radians(lat1)
    long1 = math.radians(long1)
    lat2 = math.radians(lat2)
    long2 = math.radians(long2)

    # change in longitude
    delta_long = long2 - long1

    x = math.sin(delta_long) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1) * math.cos(lat2) * math.cos(delta_long))

    initial_bearing = math.atan2(x, y)
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing


if __name__ == "__main__":
    main()
