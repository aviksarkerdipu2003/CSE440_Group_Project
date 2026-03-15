import json

def load_puzzle_from_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data["initial"], data["goal"]
