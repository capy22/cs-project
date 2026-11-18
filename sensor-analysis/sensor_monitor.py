import numpy as np
import matplotlib.pyplot as plt
import random
import csv

random.seed(1000)
sensor_type = str(input("Which type do you want?"))
print(sensor_type)

num = int(input("How many readings do you want?"))
print(num)

min_sensor = int(input("what minimum sensor value do you want?"))
print(min_sensor)

max_sensor = int(input("what maximum sensor value do you want?"))
print(max_sensor)

alert_threshold = int(input("what alert threshold value do you want?"))
print(alert_threshold)

def generate():
    temperature_list = []
    for i in range(num):
        temperature=random.uniform(min_sensor, max_sensor)
        temperature_list.append(temperature)
    temperature_array = np.array(temperature_list)
    return temperature_array

def analyze(temperature_array):
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

def visualize(temperature_array):
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

def main():
    temperature_array = generate()
    analyze(temperature_array)
    visualize(temperature_array)
    save_readings("Truc.csv", temperature_array)
    
if __name__ == "__main__":
    main()







