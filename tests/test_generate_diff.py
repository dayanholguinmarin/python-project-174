from gendiff import generate_diff


def test_equal_files():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file1.json'
    assert generate_diff(file1, file2) == ""
