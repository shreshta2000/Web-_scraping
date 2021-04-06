import requests
from Task12 import scrape_movie_cast
import json
from pprint import pprint
from bs4 import BeautifulSoup
import random
import time

list1 = scrape_movie_cast()

def movie_detail():
    time_limit = random.randint(1,3)
    imdb_api = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
    time.sleep(time_limit)
    imdb_url = requests.get(imdb_api)
    Text_Data = imdb_url.json
    soup = BeautifulSoup(imdb_url.text,"html.parser")
    my_dict = {}
    list2 = []
    div = soup.find("div", class_="lister")
    body = div.find("tbody", class_="lister-list")
    name = body.find_all("tr")
    for tr in name:
        lang = []
        dire = []
        gen = []
        movies_name = tr.find("td",class_ = "titleColumn").a.get_text()
        years = tr.find("td",class_ = "titleColumn").span.get_text()
        link = tr.find("td",class_= "titleColumn").a['href']
        url = 'https://www.imdb.com' + str(link)
        rating = float(tr.find("td",class_="ratingColumn imdbRating").strong.get_text())
        time.sleep(time_limit)
        movie_url = requests.get(url)
        soup = BeautifulSoup(movie_url.text,"html.parser")
        director_name = soup.find("div",class_="credit_summary_item").a.get_text()
        dire.append(director_name)
        for_poster  = soup.find("div",class_="poster").a['href']
        movie_poster = "https://www.imdb.com/" + for_poster
        bio = soup.find("div", class_="plot_summary" )
        movie_bio = bio.find("div", class_="summary_text").get_text().strip()
        div = soup.find("div",attrs={"class":"article","id":"titleDetails"})
        more_detail = div.find_all("div")
        for i in more_detail:
            tag = i.find_all("h4")
            for j in tag:
                if "Language:" in j:
                    lan = i.find_all('a')
                    for language in lan:
                        movies_language = language.get_text()
                        lang.append(movies_language)
        time1 = soup.find("div",class_="subtext")
        runtime = time1.find("time").get_text().strip()
        hour_in_min = (int(runtime[0])) *60
        i = 0
        mins = ""
        b = (runtime[3:])
        while i < len(b):
            if b[i] == "m":
                break
            mins = mins + b[i]
            i = i + 1
        runtime_of_movie = hour_in_min + int(mins)
        movie_genre = time1.find_all("a")
        movie_genre = time1.find_all("a")
        movie_genre.pop()
        for i in movie_genre:
            genre = i.get_text()
            gen.append(genre)
        list1 = []
        cast_api = url
        cast_url = requests.get(cast_api)
        soup = BeautifulSoup(cast_url.text,"html.parser")
        table = soup.find("table","cast_list")
        td = table.find_all("td",class_="")
        for i in td:
            my_dict1 = {}
            id = i.a["href"][6:15]
            artist = i.a.get_text().strip()
            my_dict1["artist"] = artist
            my_dict1["imbd_id"] = id
            list1.append(my_dict1)
        my_dict["name"] = movies_name
        my_dict["year"] = int(years[1:5])
        my_dict["rank"] = rating
        my_dict["movie url"] = url
        my_dict["country"] = "India"
        my_dict["language"] = lang
        my_dict["director"] = dire
        my_dict["movie bio"] = movie_bio
        my_dict["poster url"] = movie_poster
        my_dict["runtime"] = runtime_of_movie
        my_dict["genre"] = gen
        my_dict["cast"] = list1
        list2.append(my_dict)
        link = link[7:16]
        print(link)
        with open("movie/" + link + ".json","w") as data:
            json.dump(list2,data,indent=4)
    return(list2)
movie_detail()
