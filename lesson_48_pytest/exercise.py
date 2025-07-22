# Lesson 48: Testing with `pytest`

# This file contains the function to be tested.
# You will create a separate test file (`test_exercise.py`) to write your tests.

def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    A palindrome is a word, phrase, number, or other sequence of characters
    which reads the same backward as forward, e.g., "madam" or "racecar".
    This function should ignore case and non-alphanumeric characters.
    """
    # Clean the text: convert to lowercase and remove non-alphanumeric characters
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Check if the cleaned text is equal to its reverse
    return cleaned_text == cleaned_text[::-1]


# --- Instructions for creating `test_exercise.py` ---

# 1.  **Create a new file named `test_exercise.py` in the same directory as this file.**

# 2.  **In `test_exercise.py`, import the `is_palindrome` function:**
#     ```python
#     from exercise import is_palindrome
#     ```

# 3.  **Write at least three test functions in `test_exercise.py` for `is_palindrome`:**
#     *   `test_simple_palindrome()`: Test with a simple palindrome (e.g., "madam").
#     *   `test_non_palindrome()`: Test with a non-palindrome (e.g., "hello").
#     *   `test_case_insensitive_palindrome()`: Test with a palindrome that has mixed casing (e.g., "Racecar").
#     *   `test_palindrome_with_spaces_and_punctuation()`: Test with a palindrome that includes spaces and punctuation (e.g., "A man, a plan, a canal: Panama").
#     *   `test_empty_string()`: Test with an empty string.

#     Example structure for a test function:
#     ```python
#     def test_simple_palindrome():
#         assert is_palindrome("madam") == True
#     ```

# 4.  **Run your tests from the terminal in this directory:**
#     ```bash
#     pytest
#     ```

# Expected output for `test_exercise.py` (you will create this file):
# ```python
# # test_exercise.py
# from exercise import is_palindrome
# import pytest

# def test_simple_palindrome():
#     assert is_palindrome("madam") == True

# def test_non_palindrome():
#     assert is_palindrome("hello") == False

# def test_case_insensitive_palindrome():
#     assert is_palindrome("Racecar") == True

# def test_palindrome_with_spaces_and_punctuation():
#     assert is_palindrome("A man, a plan, a canal: Panama") == True

# def test_empty_string():
#     assert is_palindrome("") == True
# ```