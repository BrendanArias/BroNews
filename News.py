from bs4 import BeautifulSoup
import requests
import streamlit as st

"""
# BroNews: News for Bros, by Bros
"""


def get_article(url):
    page = requests.get(url)
    page_soup = soup(page.content, 'html.parser')
    st.write(page_soup)
    
get_article(st.text_input("_Enter the url you'd like Broified_"))
