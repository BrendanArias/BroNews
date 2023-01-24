from bs4 import BeautifulSoup
import requests
import streamlit as st

"""
# BroNews: News for Bros, by Bros
"""

url = st.text_input("_Enter the url you'd like Broified_").strip("http://")

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the main article element
article = soup.find('article')

# Extract the text of the article
article_text = article.get_text()
print(article_text)
