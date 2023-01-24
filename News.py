from bs4 import BeautifulSoup
import requests
import streamlit as st

"""
# Hey
"""

url = input("Enter the url you'd like Broified")

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the main article element
article = soup.find('article')

# Extract the text of the article
article_text = article.get_text()
print(article_text)
