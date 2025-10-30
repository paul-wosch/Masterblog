"""Provide basic file handling operations like read and write."""
import json
import blog.models

JSON_INDENT = 4


def write_file(filepath, data):
    """Write the given data to the specified file."""
    with open(filepath, "w", encoding="utf-8") as file_obj:
        file_obj.write(data)


def read_file(filepath):
    """Return content of the specified file."""
    with open(filepath, "r", encoding="utf-8") as file_obj:
        return file_obj.read()


def read_json_file(filename):
    """Return data from a json file."""
    return json.loads(read_file(filename))


def write_json_file(filepath, data):
    """Write the given data to a json file."""
    data_json = json.dumps(data, indent=JSON_INDENT)
    write_file(filepath, data_json)


def main():
    """Main function for testing."""


if __name__ == "__main__":
    main()
