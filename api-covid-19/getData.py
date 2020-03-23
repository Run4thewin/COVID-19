# IMPORT REQUESTS
import requests

#IMPORT BEATIFULSOUP FOR HTML
from bs4 import BeautifulSoup

#making the request
soup = BeautifulSoup(requests.get("https://www.worldometers.info/coronavirus/country/brazil/").text, 'html.parser')

print("\n")

#getting all the data from website
for s in soup.findAll(id="maincounter-wrap"):
    print(" "+s.h1.string)
    print(" "+s.span.string+"\n\n ")

