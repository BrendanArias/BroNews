import requests
from bs4 import BeautifulSoup

def broify_text(url):
    # Get the text from the website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()

    # Replace all pronouns with "bro"
    text = text.replace(" he ", " bro ")
    text = text.replace(" she ", " bro ")
    text = text.replace(" him ", " bro ")
    text = text.replace(" her ", " bro ")
    text = text.replace(" his ", " bro's ")
    text = text.replace(" hers ", " bro's ")

    # Output the modified text
    print(text)

# Example usage:
url = input("Enter a URL: ")
broify_text(url)
