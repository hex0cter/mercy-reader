from mercy_reader import reader
from os import path


def test_reader():
    test_data_path = path.join(path.dirname(__file__), "data.json")
    obj = reader.main(
        reader.load(test_data_path),
        80,
    )
    print(reader.Format.formatter['md'](obj))
