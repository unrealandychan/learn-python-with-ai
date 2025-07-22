
# Lesson 42: Solution

from bs4 import BeautifulSoup

with open('sample.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

print("H1 Tag:", soup.h1.string)

print("\nList Items:")
for li in soup.find_all('li'):
    print(li.string)

main_content = soup.find(id="main_content")
print("\nMain Content:", main_content.string)

