import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import os

def scrape_top_list():
    if os.path.isfile("caching/" + "scraping.json"):
        with open ("caching/" + "scraping.json","r") as Data:
            caching_movie= json.load(Data)
        return(caching_movie)
    else:
        imdb_api = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
        imdb_url = requests.get(imdb_api)
        Text_Data = imdb_url.json
        soup = BeautifulSoup(imdb_url.text,"html.parser")
        my_dict = {}
        name1 = []
        div = soup.find("div", class_="lister")
        body = div.find("tbody", class_="lister-list")
        name = body.find_all("tr")
        number = 0
        for tr in name:
            number = number + 1
            movies_name = tr.find("td",class_ = "titleColumn").a.get_text()
            years = tr.find("td",class_ = "titleColumn").span.get_text()
            link = tr.find("td",class_= "titleColumn").a['href']
            url = 'https://www.imdb.com' + str(link)
            rating = float(tr.find("td",class_="ratingColumn imdbRating").strong.get_text())
            my_dict["name"] = movies_name
            my_dict["year"] = int(years[1:5])
            my_dict["position"] = int(number)
            my_dict["rank"] = rating
            my_dict["url"] = url
            name1.append(my_dict.copy())
            with open ("caching/" + "imdb_scarping.json","w") as saral:
                data = json.dump(name1,saral,indent = 4)
    return name1
scrape_top_list()