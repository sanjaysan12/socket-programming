import requests
from bs4 import BeautifulSoup
r = requests.get('http://aucek.in/')
soup = BeautifulSoup(r.text, features="lxml")
links = set()
for link in soup.find_all('a'):
    if 'aucek.in' in link.get('href'):
        links.add(link.get('href'))
print(link)