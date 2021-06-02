# utils(?)
# invert_dictionary.py


def invert_dictionary(dictionary) -> dict:
    """Create an inverted dictionary.

    Returns: A dictionary where the keys are the values of the
    original dictionary, and the new values are the original keys.
    """

    inverted_dict = {}

    for key, value in dictionary.items():
        inverted_dict.setdefault(value, list()).append(key)

    return inverted_dict
