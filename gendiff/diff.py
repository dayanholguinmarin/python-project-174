from gendiff.parsers import parse_file
from gendiff.formatters.stylish_formatter import stylish
from gendiff.formatters.plain_formatter import plain
from gendiff.formatters.json_formatter import json_formatter


def generate_diff(file1, file2, format_name='stylish'):
    data1 = parse_file(file1)
    data2 = parse_file(file2)
    diff_dict = build_diff(data1, data2)

    if format_name == 'stylish':
        return stylish(diff_dict)
    elif format_name == 'plain':
        return plain(diff_dict)
    elif format_name == 'json':
        return json_formatter(diff_dict)
    else:
        raise ValueError(f"Formato desconocido: {format_name}")


def build_diff(dict1, dict2):

    all_dict_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    result_diff_dict = {}

    for key in all_dict_keys:
        val1 = dict1.get(key)
        val2 = dict2.get(key)

        if key not in dict2:
            result_diff_dict[key] = {'status': 'removed', 'value': val1}
        elif key not in dict1:
            result_diff_dict[key] = {'status': 'added', 'value': val2}
        elif isinstance(val1, dict) and isinstance(val2, dict):
            result_diff_dict[key] = {
                'status': 'nested',
                'value': build_diff(val1, val2)
            }
        elif val1 == val2:
            result_diff_dict[key] = {'status': 'unchanged', 'value': val1}
        else:
            result_diff_dict[key] = {
                'status': 'changed',
                'old_value': val1,
                'new_value': val2
            }

    return result_diff_dict
