from gendiff import generate_diff


def test_flat_yaml_diff():
    file1 = "tests/fixtures/file1.yml"
    file2 = "tests/fixtures/file2.yml"
    expected = """{
      - follow: false
        host: hexlet.io
      - proxy: 123.234.53.22
      - timeout: 50
      + timeout: 20
      + verbose: true
    }"""
    result = generate_diff(file1, file2)
    assert result == expected


def test_equal_yaml_files():
    file1 = "tests/fixtures/file1.yml"
    file2 = "tests/fixtures/file1.yml"
    assert generate_diff(file1, file2) == ""
