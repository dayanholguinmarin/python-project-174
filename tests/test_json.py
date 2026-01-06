from gendiff import generate_diff
import pathlib


def read_expected(filename):
    path = pathlib.Path('tests/fixtures') / filename
    return path.read_text().strip()


def test_diff_files_json():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    expected = read_expected('expected_diff.txt')
    assert generate_diff(file1, file2) == expected


def test_equal_files_json():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file1.json'
    assert generate_diff(file1, file2) == ""
