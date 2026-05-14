# Lesson 48: Testing with `pytest`

`pytest` is a powerful and popular testing framework for Python. It makes it easy to write simple, readable tests and scales well for complex functional testing. Compared to Python's built-in `unittest` module, `pytest` often requires less boilerplate code and offers more advanced features.

**Official Documentation:** [https://docs.pytest.org/en/stable/](https://docs.pytest.org/en/stable/)

---

### Installation

If you don't have `pytest` installed, you can do so using pip:

```bash
pip install pytest
```

### Basic Test Structure

`pytest` automatically discovers tests based on certain conventions:

*   **Test Files**: Files should be named `test_*.py` or `*_test.py`.
*   **Test Functions**: Functions inside test files should start with `test_`.
*   **Test Classes**: Classes can start with `Test` (e.g., `TestMyFeature`), and methods inside them should start with `test_`.

**Example `my_functions.py`:**

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

**Example `test_my_functions.py`:**

```python
from my_functions import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 10) == 0
    assert subtract(0, 5) == -5
```

### Running Tests

To run your tests, navigate to your project directory in the terminal and simply type `pytest`:

```bash
pytest
```

`pytest` will discover and run all tests in the current directory and its subdirectories that follow the naming conventions. It will report the number of passed, failed, and skipped tests.

### Assertions

`pytest` uses the standard Python `assert` statement for making assertions. When an `assert` statement fails, `pytest` provides detailed information about the values involved, making debugging easier.

```python
def test_equality():
    a = 5
    b = 10
    assert a == b, "a and b should be equal"

def test_in_list():
    my_list = [1, 2, 3]
    assert 4 in my_list, "4 should be in the list"
```

### Fixtures

Fixtures are functions that `pytest` runs before (and sometimes after) your test functions. They are used to set up a test environment (e.g., create a temporary file, connect to a database, prepare data) and clean it up afterwards. Fixtures are defined using the `@pytest.fixture` decorator.

```python
import pytest

@pytest.fixture
def sample_data():
    # Setup: This data will be available to tests that request it
    data = [1, 2, 3, 4, 5]
    print("\nSetup: Sample data created")
    yield data # Yield the data to the test function
    # Teardown: This code runs after the test function finishes
    print("Teardown: Sample data cleaned up")

def test_data_length(sample_data):
    assert len(sample_data) == 5

def test_data_sum(sample_data):
    assert sum(sample_data) == 15
```

### Parametrization

Parametrization allows you to run the same test function multiple times with different sets of arguments. This is very useful for testing various inputs and edge cases without writing repetitive code.

```python
import pytest

@pytest.mark.parametrize("input_a, input_b, expected_sum", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (10, -5, 5)
])
def test_add_parametrized(input_a, input_b, expected_sum):
    assert (input_a + input_b) == expected_sum
```

### Skipping Tests and Expected Failures

*   **`pytest.mark.skip`**: Skips a test unconditionally or based on a condition.
*   **`pytest.mark.xfail`**: Marks a test as expected to fail. If it fails, it's reported as `xfailed`. If it passes, it's reported as `xpassed`.

```python
import pytest

@pytest.mark.skip(reason="This feature is not ready yet")
def test_incomplete_feature():
    assert False # This test will be skipped

@pytest.mark.xfail(reason="Known bug #123")
def test_buggy_function():
    result = 1 / 0 # This will cause an error, but it's expected to fail
    assert result == 0
```

### Good Practices for Writing Tests

*   **Independent Tests**: Each test should be independent and not rely on the order of execution or the state left by other tests.
*   **Clear Naming**: Use descriptive names for test files, functions, and classes.
*   **Arrange-Act-Assert (AAA)**: A common pattern for structuring tests:
    *   **Arrange**: Set up the test data and environment.
    *   **Act**: Perform the action you want to test.
    *   **Assert**: Verify the outcome of the action.
*   **Test One Thing**: Each test should ideally focus on testing a single piece of functionality.

---

### Quiz

1.  **By default, what prefix should test functions have in `pytest`?**
    a) `_test`
    b) `Test`
    c) `test_`

2.  **What command do you run in the terminal to execute your `pytest` tests?**
    a) `python -m pytest`
    b) `run_tests`
    c) `pytest`

3.  **What is the purpose of a `pytest` fixture?**
    a) To define a test case.
    b) To set up a test environment and clean it up.
    c) To skip a test.

4.  **How can you run the same test function with different inputs without writing repetitive code?**
    a) Using `pytest.mark.skip`
    b) Using `pytest.mark.parametrize`
    c) Using `pytest.fixture`

<details>
  <summary><b>Answer Key</b></summary>
  1. c
  2. c
  3. b
  4. b
</details>