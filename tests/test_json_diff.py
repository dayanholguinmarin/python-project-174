from gendiff import generate_diff


def test_diff_files_json():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    expected = """{
      - proxy: 123.234.53.22
      - timeout: 50
      + timeout: 20
      + verbose: true
    }"""
    assert generate_diff(file1, file2) == expected