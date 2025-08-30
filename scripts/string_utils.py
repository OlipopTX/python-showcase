"""
String utilities example for python-showcase.

This script demonstrates simple string manipulation functions.
"""


def reverse_string(s: str) -> str:
    """Return the reverse of the input string."""
    return s[::-1]


def count_vowels(s: str) -> int:
    """Return the number of vowels in the input string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


def is_palindrome(s: str) -> bool:
    """Check if the input string is a palindrome (reads the same forwards and backwards)."""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    example = "OpenAI"
    print("Reverse:", reverse_string(example))
    print("Vowel count:", count_vowels(example))
    palindrome_example = "Madam"
    print(f"Is '{palindrome_example}' a palindrome?:", is_palindrome(palindrome_example))
