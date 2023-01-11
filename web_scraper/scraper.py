import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Super_Mario_Bros.'

def get_citations(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    citations = soup.find_all('span', text='citation needed')
    return len(citations)

print(get_citations(url))