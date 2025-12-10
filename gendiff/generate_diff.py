import json
from gendiff.parsers import parse_file

# def read_json(file_path):
    # with open(file_path) as f:
        # return json.load(f)


def generate_diff(file1, file2):

    dict1 = parse_file(file1)
    dict2 = parse_file(file2)

    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    result_diff = ['{']

    for key in all_keys:
        val1 = dict1.get(key)
        val2 = dict2.get(key)

        if val1 == val2:
            result_diff.append(f"    {key}: {val1}")
        elif key in dict1 and key not in dict2:
            result_diff.append(f"  - {key}: {val1}")
        elif key not in dict1 and key in dict2:
            result_diff.append(f"  + {key}: {val2}")
        else:
            result_diff.append(f"  - {key}: {val1}")
            result_diff.append(f"  + {key}: {val2}")

    result_diff.append('}')

    return "\n".join(result_diff)
