# Lesson 42: `BeautifulSoup4` - Web Scraping

from bs4 import BeautifulSoup
import os

def parse_html_file(filepath):
    """
    Reads an HTML file and parses it with BeautifulSoup.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
        soup = BeautifulSoup(html_content, 'lxml') # Using lxml parser for efficiency
        return soup
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"An error occurred while parsing the file: {e}")
        return None

def main():
    # Construct the absolute path to sample.html
    current_dir = os.path.dirname(__file__)
    html_filepath = os.path.join(current_dir, 'sample.html')

    soup = parse_html_file(html_filepath)

    if soup:
        print("\n--- Task 1: Find and print the text of the <h1> tag ---")
        # Your code here
        h1_tag = soup.find('h1')
        if h1_tag:
            print(f"H1 Tag Text: {h1_tag.get_text()}")
        else:
            print("H1 tag not found.")

        print("\n--- Task 2: Find all <li> tags and print their text ---")
        # Your code here
        li_tags = soup.find_all('li')
        if li_tags:
            print("List Items:")
            for li in li_tags:
                print(f"- {li.get_text()}")
        else:
            print("No list items found.")

        print("\n--- Task 3: Find the tag with the id of \"main_content\" and print its text ---")
        # Your code here
        main_content_tag = soup.find(id='main_content')
        if main_content_tag:
            print(f"Main Content Text: {main_content_tag.get_text()}")
        else:
            print("Tag with id 'main_content' not found.")

        print("\n--- Task 4: Find all elements with the class \"highlight\" and print their text ---")
        # Your code here (Hint: use class_ argument or CSS selector)
        highlight_elements = soup.find_all(class_='highlight')
        if highlight_elements:
            print("Highlighted Elements:")
            for element in highlight_elements:
                print(f"- {element.get_text()}")
        else:
            print("No elements with class 'highlight' found.")

        print("\n--- Task 5: Find the text of the first <a> tag within the <footer> ---")
        # Your code here (Hint: use CSS selectors or chained find calls)
        footer_link = soup.select_one('footer a')
        if footer_link:
            print(f"Footer Link Text: {footer_link.get_text()}")
        else:
            print("No link found in footer.")

if __name__ == "__main__":
    main()