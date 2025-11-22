import json
import os

# Load data from JSON file
def load_data(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r") as f:
        return json.load(f)

# Save data to JSON file
def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
