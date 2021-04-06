import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup
api = "https://webscraper.io/test-sites"
url = requests.get(api)
Data = url.json
soup = BeautifulSoup(url.text,"html.parser")
div = soup.find("div",class_="container test-sites")
name = div.find_all("div",class_="col-md-7 pull-right")
for i in name:
    name1 = i.a.get_text().strip()
    print(name1) 