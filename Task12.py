import requests
from Task1 import scrape_top_list
import json
from pprint import pprint
from bs4 import BeautifulSoup

name1 = scrape_top_list()
def scrape_movie_cast():
    list1 = []
    movie = 10
    cast_api = name1[movie]["url"]
    cast_url = requests.get(cast_api)
    soup = BeautifulSoup(cast_url.text,"html.parser")
    table = soup.find("table","cast_list")
    td = table.find_all("td",class_="")
    for i in td:
        my_dict = {}
        id = i.a["href"][6:15]
        artist = i.a.get_text().strip()
        my_dict["artist"] = artist
        my_dict["imbd_id"] = id
        list1.append(my_dict)
    with open("artist_name.json","w") as name:
        json.dump(list1,name,indent=4)
    return(list1) 
scrape_movie_cast()
    