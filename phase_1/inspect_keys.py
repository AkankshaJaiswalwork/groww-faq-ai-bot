import json
import os

def inspect():
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    for file in os.listdir(data_dir):
        if file.endswith("_structured.json"):
            with open(os.path.join(data_dir, file), "r") as f:
                data = json.load(f)
                print(f"File: {file}")
                print(f"Keys: {list(data.keys())}")
                print("-" * 40)

if __name__ == "__main__":
    inspect()
