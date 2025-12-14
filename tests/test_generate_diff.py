from gendiff import generate_diff


def test_equal_files():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file1.json'
    assert generate_diff(file1, file2) == {}


def test_diff_files_json():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    with open('tests/fixtures/expected_diff.txt') as f:
        expected_diff = f.read().strip()
    assert generate_diff(file1, file2) == expected_diff


def test_diff_files_yaml():
    file1 = 'tests/fixtures/file1.yml'
    file2 = 'tests/fixtures/file2.yml'
    with open('tests/fixtures/expected_diff.txt') as f:
        expected_diff = f.read().strip()
    assert generate_diff(file1, file2) == expected_diff
