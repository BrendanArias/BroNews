import requests
from bs4 import BeautifulSoup
import streamlit as st

# UI Text

"""
# BroNews: _News for Bros, by Bros_
"""

# Set the URL that you want to make a request to.
article_url = st.text_input("_Enter an article's URL:_")

def broify():
    # Make the request and store the response.
    response = requests.get(article_url)
    
    # Parse the HTML content of the website.
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract the text from the website and print it.
    for p in soup.find_all("body", {"type": "article"}):
        text += p.text
   
    # Feed the summarization text to the app
    st.write("Alright Bro, so basically...")
    st.write(text)
    
if article_url:
    # Text generation spinner
    with st.spinner("Please wait while your summary is being generated..."):
        # Generate the summarization text
    broify()


