import os
import csv

def average_temp_from_csv(filename):
    base_dir = os.path.dirname(__file__)  # folder where this script is
    path = os.path.join(base_dir, "..", "data", filename)  # go up 1 level, then into data/
    
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        temps = [float(row['temperature']) for row in reader]
        return sum(temps) / len(temps)

# Run
avg = average_temp_from_csv("temperatures.csv")
print("Average temperature:", avg)
