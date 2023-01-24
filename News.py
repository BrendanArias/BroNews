import requests
import BeautifulSoup
import streamlit as st

"""
# BroNews: _For the bros, by the bros_
"""
url = input("Enter the url you'd like Broified")

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the main article element
article = soup.find('article')

# Extract the text of the article
article_text = article.get_text()
print(article_text)
