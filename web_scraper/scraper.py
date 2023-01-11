import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Super_Mario_Bros.'

def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    citations = soup.find_all('span', text='citation needed')
    return len(citations)

print(get_citations_needed_count(url))

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    citations = soup.find_all('span', text='citation needed')
    parents = []
    statements = []
    for cit in citations:
        parents.append(cit.findParent('p'))

    report = 'Citations are needed for the following:\n\n'

    for cit in parents:
        report += f'{cit.text}\n'
        statements.append(cit.text.strip())

    return report, statements

print(get_citations_needed_report(url))