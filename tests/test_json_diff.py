from gendiff import generate_diff
import json


def load_fixtures(file_name):
    with open(f"tests/fixtures/{file_name}") as f:
        return f.read()


def test_json_diff():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    expected_diff = load_fixtures('expected_diff.txt')

    result = generate_diff(file1, file2, format='json')

    parsed_result = json.loads(result)
    parsed_expected = json.loads(expected_diff)

    assert parsed_result == parsed_expected
