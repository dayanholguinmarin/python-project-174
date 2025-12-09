from gendiff import generate_diff

def load_fixtures(file_name):
    with open(f"tests/fixtures/{file_name}") as f:
        return f.read()


def test_json_diff():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    expected_diff = load_fixtures('expected_diff.txt')

    assert generate_diff(file1, file2) == expected_diff
    