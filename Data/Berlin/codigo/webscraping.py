import requests
from bs4 import BeautifulSoup

URL = 'https://www.speedtest.net/global-index'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('table', class_="country-results")
print(results.prettify())