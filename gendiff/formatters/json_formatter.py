import json


def json_formatter(diff_dict):
    """
    Convierte el árbol de diferencias en un string JSON.
    """
    return json.dumps(diff_dict, indent=4)
