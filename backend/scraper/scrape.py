import requests
from bs4 import BeautifulSoup

def extract_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for script in soup(["script", "style"]):
        script.decompose()
    return " ".join(soup.stripped_strings)
