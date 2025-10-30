"""Provide functions to keep track of auto-incremented primary keys."""
from pathlib import Path
from filestore import read_json_file, write_json_file

SEQUENCE_FILE = Path("sequence.json")
DATA_DIR = Path("../data")
SEQUENCE_FILE_PATH = DATA_DIR / SEQUENCE_FILE


def get_next_id(model: str) -> int:
    """Return auto-incremented unique id for the given model
    or None if model is not found.

    Also, update the new id in the sequence dict and save it persistently.
    """
    id = read_json_file(SEQUENCE_FILE_PATH).get(model, None)
    if id:
        id += 1
    return id


def save_id_to_sequence(model: str, id: int):
    """Save the given id for a model persistently."""
    # load data
    data = read_json_file(SEQUENCE_FILE_PATH)
    # update data only for valid model and id
    if id and data.get(model) and isinstance(id, int):
        data[model] = id
        write_json_file(SEQUENCE_FILE_PATH, data)


def main():
    """Main function for testing."""


if __name__ == "__main__":
    main()
