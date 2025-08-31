"""
Data structures example for python-showcase.

This script demonstrates basic usage of lists and dictionaries in Python.
"""


def list_example():
    """Return a list of squared numbers from 1 to 5."""
    return [i ** 2 for i in range(1, 6)]


def dict_example():
    """Return a dictionary mapping numbers to their squares."""
    return {i: i ** 2 for i in range(1, 6)}


if __name__ == "__main__":
    print("List example:", list_example())
    print("Dict example:", dict_example())
