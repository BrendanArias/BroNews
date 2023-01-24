import requests
from bs4 import BeautifulSoup4

url = "https://www.foxnews.com/politics/democratic-house-leader-hakeem-jeffries-demands-mccarthy-reappoint-schiff-swalwell-intelligence-committee"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the main article element
article = soup.find('article')

# Extract the text of the article
article_text = article.get_text()
print(article_text)
