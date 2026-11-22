This repository is the assignment 1 of the course of Control System.

# Assignment 1
## How to run
Go to sensor-analysis folder, and run  `python3 sensor_monitor.py`.

## What it does
The program asks the user choose between generating new sensor readings based on `random.seed(1000)`, or loading reading from an existing CSV file.

The program always asks the user to enter:

- Sensor type (for example, temperature or light).
- Number of readings to generate.
- Minimum sensor value.
- Maximum sensor value.
- Alert threshold.

Then it analyzes the data and visualize it with 2 graphs: Line plot and Histogram.

If the user loads existing data, analyze and plot that data without generating new readings.