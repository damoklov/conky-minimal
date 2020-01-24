import urllib.request
import json
import re
from bs4 import BeautifulSoup


# Open a webpage and retrieve its content

wp = urllib.request.urlopen('https://www.instagram.com/bulletinoftheatomicscientists/')
wpText = wp.read().decode()

# Find a needed part

soup = BeautifulSoup(wpText, 'html.parser')
text = soup.head.find('script', attrs={'type': 'application/ld+json'}).find_all(text=True, recursive=False)[0].strip()
jsonObject = json.loads(text)

 # Find all words in capital letters

regex = r"\b[A-Z0-9]+\b"
matches = re.finditer(regex, jsonObject['description'])

print(' '.join([match[0] for match in matches]))
