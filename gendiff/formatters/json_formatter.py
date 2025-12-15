import json


def json_formatter(diff_dict):
    return json.dumps(diff_dict, indent=4)
