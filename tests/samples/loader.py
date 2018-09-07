import json
import os


def load_sample(filename='test_result.json'):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    abs_file_path = os.path.join(root_dir, filename)
    with open(abs_file_path) as f:
        return json.load(f)
