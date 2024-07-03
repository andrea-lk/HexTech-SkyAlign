import tkinter as tk
import subprocess

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
turntable_process = None


def main():
    global turntable_process
    # Start the turntable script in a separate process
    turntable_process = subprocess.Popen(["python", "turn_table.py"])

    # create the window
    window = tk.Tk()
    geometry = f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
    window.geometry(geometry)
    window.title("Drone GPS Coordinates")

    # create the input boxes and buttons
    entries = create_input_boxes(window)
    make_buttons(window, entries)

    window.mainloop()

    # Terminate the turntable process when the GUI window is closed
    turntable_process.terminate()


def create_input_boxes(window):
    labels_texts = ["Enter Turntable Latitude: ", "Enter Turntable Longitude: ", "Enter Drone Latitude: ", "Enter Drone Longitude: "]
    entries = []

    for i, label_text in enumerate(labels_texts):
        label = tk.Label(window, text=label_text, font=("Comic Sans", 20))
        label.grid(row=i, column=0, padx=10, pady=10, sticky='E')

        entry = tk.Entry(window, font=("Comic Sans", 20))
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries.append(entry)

    return entries


def make_buttons(window, entries):
    submit_button = tk.Button(window, text="Submit", command=lambda: submit(entries))
    submit_button.grid(row=len(entries), column=0, padx=10, pady=10, sticky='E')

    clear_button = tk.Button(window, text="Clear", command=lambda: clear(entries))
    clear_button.grid(row=len(entries), column=1, padx=10, pady=10, sticky='W')


def submit(entries):
    turntable_lat = entries[0].get()
    turntable_long = entries[1].get()
    drone_lat = entries[2].get()
    drone_long = entries[3].get()

    print(f"Turntable GPS coordinates:\nLatitude = {turntable_lat},\nLongitude = {turntable_long}")
    print(f"Drone GPS coordinates:\nLatitude = {drone_lat},\nLongitude = {drone_long}")

    with open("coordinates.txt", "w") as file:
        file.write(f"{turntable_lat},{turntable_long},{drone_lat},{drone_long}")

    # Run calculations.py to compute the steps
    subprocess.run(["python", "calculations.py"])


def clear(entries):
    for entry in entries:
        entry.delete(0, tk.END)


if __name__ == "__main__":
    main()
