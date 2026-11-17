import random
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
    print(temperature_list)
    print(0)
    return temperature_list

def main():
    generate()

if __name__ == "__main__":
    main()







