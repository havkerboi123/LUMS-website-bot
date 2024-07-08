import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to get all links from a webpage
def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
    
    return links

links=get_links("https://www.lums.edu.pk")
with open('pk_links.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')

