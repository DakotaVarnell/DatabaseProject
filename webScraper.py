import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/search/title/?sort=num_votes,desc&start=1&title_type=feature&year=1950,2012"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())

for movie in soup.findAll('td','title'):
    title = movie.find('a').contents[0]
    print(title)

#soupUrl = soup.findAll("meta", property="og:url")
