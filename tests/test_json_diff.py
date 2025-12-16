from gendiff import generate_diff


def test_diff_files_json():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    expected = """{
      common: {
        + follow: false
        - setting2: 200
        - setting3: true
        + setting3: null
        + setting4: blah blah
        + setting5: {
              key5: value5
          }
          setting6: {
              doge: {
                - wow: 
                + wow: so much
              }
            + ops: vops
          }
      }
      group1: {
        - baz: bas
        + baz: bars
        - nest: {
              key: value
          }
        + nest: str
      }
    - group2: {
          abc: 12345
          deep: {
              id: 45
          }
      }
    + group3: {
          deep: {
              id: {
                  number: 45
              }
          }
          fee: 100500
      }
    }"""
    assert generate_diff(file1, file2) == expected
