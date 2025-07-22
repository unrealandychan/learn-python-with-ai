# Lesson 42: `BeautifulSoup4` - Web Scraping with HTML Parsing

Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.

**Official Documentation:** [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

---

### Installation

If you don't have `BeautifulSoup4` installed, you can do so using pip. You'll also need a parser; `lxml` is a good choice for performance.

```bash
pip install beautifulsoup4 lxml
```

### Basic Usage: Parsing HTML

To start, you need to create a `BeautifulSoup` object by passing the HTML content and the parser you want to use.

```python
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body></html>
"""

soup = BeautifulSoup(html_doc, 'lxml') # Using 'lxml' parser

# Pretty-printing the HTML
# print(soup.prettify())
```

### Navigating the Parse Tree

Once you have a `BeautifulSoup` object, you can navigate the HTML structure like a tree.

#### By Tag Name

You can access tags directly as attributes of the `soup` object. This will give you the *first* occurrence of that tag.

```python
# print(soup.title) # <title>The Dormouse's story</title>
# print(soup.title.name) # title
# print(soup.title.string) # The Dormouse's story
# print(soup.p) # <p class="title"><b>The Dormouse's story</b></p>
```

#### Contents and Children

*   `.contents`: A list of the tag's direct children.
*   `.children`: An iterator for the tag's direct children.
*   `.descendants`: An iterator for all children, grandchildren, etc.

```python
# head_tag = soup.head
# print(head_tag.contents) # [<title>The Dormouse's story</title>]

# for child in soup.body.children:
#     print(child)
```

#### Parents and Siblings

*   `.parent`: The parent of a tag.
*   `.parents`: An iterator for all ancestors.
*   `.next_sibling`, `.previous_sibling`: The next/previous element at the same level.
*   `.next_elements`, `.previous_elements`: Iterators for all following/preceding elements.

```python
# title_tag = soup.title
# print(title_tag.parent.name) # head

# link2_tag = soup.find(id="link2")
# print(link2_tag.next_sibling) # and
# print(link2_tag.previous_sibling) # Elsie
```

### Searching the Tree

Beautiful Soup provides powerful methods for searching the parse tree.

#### `find()` and `find_all()`

*   `find(name, attrs, recursive, text, **kwargs)`: Finds the *first* tag that matches the criteria.
*   `find_all(name, attrs, recursive, text, limit, **kwargs)`: Finds *all* tags that match the criteria.

**Searching by Tag Name:**

```python
# all_paragraphs = soup.find_all('p')
# for p in all_paragraphs:
#     print(p.text)
```

**Searching by Attributes (e.g., `class`, `id`):**

```python
# title_paragraph = soup.find('p', class_='title') # Note: class_ because class is a Python keyword
# print(title_paragraph.text)

# link_by_id = soup.find(id='link1')
# print(link_by_id.text)
```

**Searching by Text Content:**

```python
# story_text = soup.find(text="Once upon a time there were three little sisters; and their names were")
# print(story_text)
```

#### CSS Selectors with `select()` and `select_one()`

If you're familiar with CSS selectors, Beautiful Soup allows you to use them directly.

*   `select(selector)`: Returns a list of all elements matching the CSS selector.
*   `select_one(selector)`: Returns the first element matching the CSS selector.

```python
# Select all <a> tags within a <p> tag with class "story"
# links = soup.select('p.story a')
# for link in links:
#     print(link.get('href'))

# Select the element with id "link2"
# link2 = soup.select_one('#link2')
# print(link2.text)

# Select elements with class "sister"
# sisters = soup.select('.sister')
# for sister in sisters:
#     print(sister.text)
```

### Extracting Data

*   **`.string` or `.text` or `.get_text()`**: To get the text content of a tag.
*   **`tag['attribute_name']` or `tag.get('attribute_name')`**: To get the value of an attribute.

```python
# link_tag = soup.find('a', id='link1')
# print(link_tag.text) # Elsie
# print(link_tag['href']) # http://example.com/elsie
```

---

### Quiz

1.  **What is the primary purpose of `BeautifulSoup`?**
    a) To make HTTP requests.
    b) To parse HTML/XML and extract data.
    c) To build web applications.

2.  **Which method would you use to find all `<div>` tags with a specific class `product-item`?**
    a) `soup.find('div', class_='product-item')`
    b) `soup.find_all('div', class_='product-item')`
    c) `soup.select('div.product-item')`
    d) Both b and c

3.  **How do you get the text content of a tag named `<h1>`?**
    a) `soup.h1.string`
    b) `soup.h1.text`
    c) `soup.h1.get_text()`
    d) All of the above

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. d
  3. d
</details>