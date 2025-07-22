# Lesson 50: uv - Exercise

## Objective
This exercise guides you through a typical workflow using `uv` for managing a Python project's dependencies and virtual environment.

## Instructions

1.  **Create a new project directory:**
    Create a new directory for this exercise (e.g., `uv_project_exercise`) and navigate into it.

    ```bash
    mkdir uv_project_exercise
    cd uv_project_exercise
    ```

2.  **Initialize a virtual environment:**
    Use `uv` to create a new virtual environment within this directory.

    ```bash
    uv venv
    ```

3.  **Activate the virtual environment:**
    Activate the newly created virtual environment.

    *   **Linux/macOS:**
        ```bash
        source .venv/bin/activate
        ```
    *   **Windows (Command Prompt):**
        ```bash
        .venv\Scripts\activate.bat
        ```
    *   **Windows (PowerShell):**
        ```bash
        .venv\Scripts\Activate.ps1
        ```

4.  **Define project dependencies:**
    Create a `pyproject.toml` file in your `uv_project_exercise` directory with the following content. This file will declare your direct project dependencies.

    ```toml
    # pyproject.toml
    [project]
    name = "my-uv-app"
    version = "0.1.0"
    dependencies = [
        "requests~=2.31",
        "beautifulsoup4~=4.12",
        "lxml~=4.9",
    ]
    ```

5.  **Compile dependencies:**
    Use `uv` to compile your dependencies and create a `uv.lock` file. This will resolve all transitive dependencies and pin their exact versions.

    ```bash
    uv pip compile
    ```
    Inspect the generated `uv.lock` file. You'll see a comprehensive list of all packages and their versions.

6.  **Synchronize the environment:**
    Install all the dependencies listed in `uv.lock` into your virtual environment.

    ```bash
    uv pip sync
    ```

7.  **Verify installation:**
    Write a small Python script (e.g., `app.py`) to confirm that `requests` and `beautifulsoup4` are installed and working correctly.

    ```python
    # app.py
    import requests
    from bs4 import BeautifulSoup

    def fetch_title(url):
        try:
            response = requests.get(url)
            response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
            soup = BeautifulSoup(response.text, 'lxml')
            title = soup.title.string if soup.title else "No title found"
            print(f"Title of {url}: {title}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")

    if __name__ == "__main__":
        print("Testing requests and BeautifulSoup4...")
        fetch_title("https://www.python.org")
        fetch_title("https://www.example.com")
        print("Done.")
    ```

    Run the script:

    ```bash
    python app.py
    ```

    You should see the titles of the respective websites printed to the console.

8.  **Clean up (Optional):**
    When you are done, you can remove the virtual environment and the project directory.

    ```bash
    deactivate # If activated
    cd ..
    rm -rf uv_project_exercise
    ```

This exercise demonstrates the power and simplicity of `uv` for managing your Python project dependencies from environment creation to reproducible installations.