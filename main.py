import requests
from bs4 import BeautifulSoup

# url of website to scrape
url = "https://www.imdb.com/chart/moviemeter/"
# For bypassing block
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'
}

# get the html from the website
response = requests.get(url, headers=headers)

# parse the html using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup)
# Extracting the relevant information from the html code
movies = []
for row in soup.select("ul.ipc-metadata-list li"):
    title = row.find("div", class_="sc-b189961a-0").find('a').get_text()
    print(title)
