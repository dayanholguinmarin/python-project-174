import json
import yaml
import os

def parse_file(file_path):
    """Parses a file and returns its content as a dictionary."""
    _, ext = os.path.splitext(file_path)
    with open(file_path) as f:
        if ext in ['.yml', '.yaml']:
            return yaml.safe_load(f)
        elif ext == '.json':
            return json.load(f)
        else:
            raise ValueError(f"Unsupported file format: {ext}")