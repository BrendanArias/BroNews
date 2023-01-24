from bs4 import BeautifulSoup
import requests
import streamlit as st

"""
# BroNews: News for Bros, by Bros
"""

url = st.text_input("_Enter the url you'd like Broified_")

def get_article(url):
    page = requests.get(url)
    page_soup = soup(page.content, 'html.parser')
    print(page_soup)

