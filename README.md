# Beautiful Soup Example Project

This project demonstrates how to use [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for web scraping in Python.

## Installation

Install the required dependencies:

```bash
pip install beautifulsoup4 requests
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Example: print all links
for link in soup.find_all("a"):
    print(link.get("href"))

