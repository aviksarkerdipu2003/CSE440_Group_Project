import json

def load_maze_from_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data["grid"], tuple(data["start"]), tuple(data["goal"])
