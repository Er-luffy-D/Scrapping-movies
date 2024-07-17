import requests
from bs4 import BeautifulSoup

# url of website to scrape
url = "https://www.imdb.com/chart/moviemeter/"

# get the html from the website
response = requests.get(url)

# parse the html using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
