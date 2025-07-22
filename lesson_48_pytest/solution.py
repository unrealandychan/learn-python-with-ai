
# Lesson 48: Solution (in test_exercise.py)

from exercise import is_palindrome

def test_simple_palindrome():
    assert is_palindrome("racecar") == True

def test_non_palindrome():
    assert is_palindrome("hello") == False

def test_casing_palindrome():
    assert is_palindrome("Racecar") == True
