import numpy as np
import matplotlib.pyplot as plt
import random
import csv
from pathlib import Path

def get_user_input():
    try:
        random.seed(1000)
        sensor_type = str(input("Which type do you want?"))
        print(sensor_type)

        num = int(input("How many readings do you want?"))
        if num <= 0:
            raise ValueError("Please enter a positive number.")

        min_sensor = int(input("what minimum sensor value do you want?"))
        max_sensor = int(input("what maximum sensor value do you want?"))
        if min_sensor > max_sensor:
            raise ValueError("Please enter minimum sensor value smaller than maximum sensor value.")

        alert_threshold = int(input("what alert threshold value do you want?"))
        print(alert_threshold)
        return num, min_sensor, max_sensor, alert_threshold
    except ValueError as error:
        raise ValueError("Please enter a number instead of a text")

def generate(num, min_sensor, max_sensor):
    temperature_list = []
    for i in range(num):
        temperature=random.uniform(min_sensor, max_sensor)
        temperature_list.append(temperature)
    temperature_array = np.array(temperature_list)
    return temperature_array

def analyze(temperature_array, alert_threshold):
    print(temperature_array)
    print("Number of elements:",temperature_array.size)
    print("Mean", np.mean(temperature_array))
    print("Minimum:", np.min(temperature_array))
    print("Maximum:", np.max(temperature_array))
    print("Standard deviation:", np.std(temperature_array))
    mask = temperature_array > alert_threshold
    print("Mask:", mask)
    high_reading = temperature_array[mask]
    print("Readings above threshold:", high_reading)
    print("Number of high readings:", len(high_reading))

def visualize(temperature_array, alert_threshold):
    sample_number = np.arange(len(temperature_array))
    threshold = alert_threshold
    plt.plot(
        sample_number,
        temperature_array,
        marker = "x",
        label = "degree Celsius"
    )
    plt.axhline(
        threshold,
        linestyle = "--",
        label = "Threshold"
    )
    plt.xlabel("Sample number")
    plt.ylabel("degree Celsius")
    plt.title("Sensor Readings")
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.hist(temperature_array, bins = 4, edgecolor = "black")
    plt.xlabel("degree Celsius")
    plt.ylabel("Occurrences")
    plt.title("Distribution of Sensor Readings")
    plt.grid(axis = "y")
    plt.show()

def save():
    with open("notes.txt", "w", encoding="utf-8") as file:
        file.write("Sensor test started\n")
        file.write("These are simulated readings\n")
    print("Text file saved.")    

def save_readings(filename, readings):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["sample", "degree Celsius"])

        for sample_number, temperature in enumerate(readings, start=1):
            writer.writerow([sample_number, temperature])

def load_temperature_data(filename):
    temperature = []

    with open(filename, "r", newline = "", encoding = "utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            temperature.append(float(row["degree Celsius"]))
    if not temperature:
        raise ValueError(" The CSV file contains no readings.")
    return np.array(temperature, dtype = float)

def main():
    csv_path = Path("Truc.csv")
    num, min_sensor, max_sensor, alert_threshold = get_user_input()
    if csv_path.exists():
        try:
            temperature = load_temperature_data(csv_path)
            print(f"Loaded {len(temperature)} readings from {csv_path}")
            analyze(temperature, alert_threshold)
            visualize(temperature, alert_threshold)

        except (OSError) as error:
            print("Could not load the CSV:", error)
        except (ValueError) as error:
            print("Invalid input:", error)

    else:
        temperature_array = generate(num, min_sensor, max_sensor)
        analyze(temperature_array, alert_threshold)
        visualize(temperature_array, alert_threshold)
        try:
            save_readings("Truc.csv", temperature_array)

        except(OSError) as error:
            raise OSError ("Could not save the CSV file.", error)
        
    
if __name__ == "__main__":
    main()







