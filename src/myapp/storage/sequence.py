"""Provide functions to keep track of auto-incremented primary keys."""
from myapp.storage import read_json_file, write_json_file
from myapp.config import SEQUENCE_FILE_PATH


def get_next_id(model: str) -> int:
    """Return auto-incremented unique id for the given model
    or None if model is not found.

    Also, update the new id in the sequence dict and save it persistently.
    """
    post_id = read_json_file(SEQUENCE_FILE_PATH).get(model, None)
    if post_id:
        post_id += 1
    return post_id


def save_id_to_sequence(model: str, post_id: int):
    """Save the given id for a model persistently."""
    # load data
    data = read_json_file(SEQUENCE_FILE_PATH)
    # update data only for valid model and id
    if post_id and data.get(model) and isinstance(post_id, int):
        data[model] = post_id
        write_json_file(SEQUENCE_FILE_PATH, data)


def main():
    """Main function for testing."""


if __name__ == "__main__":
    main()
