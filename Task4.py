from Task1 import scrape_top_list
import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup

details = {}
dire = []
lang = []
gen = []
name1 = scrape_top_list()
def scrape_movie_details():
    movie = int(input("entre any movie number 1 to 250 : "))
    movies_name = name1[movie-1]["name"]
    movie_api = name1[movie-1]["url"]
    movie_url = requests.get(movie_api)
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
    time = soup.find("div",class_="subtext")
    runtime = time.find("time").get_text().strip()
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
    movie_genre = time.find_all("a")
    movie_genre.pop()
    for i in movie_genre:
        genre = i.get_text()
        gen.append(genre)
    details["movie_name"] = name1[movie-1]["name"]
    details["director"] = dire
    details["country"] = "India"
    details["poster_url"] = movie_poster
    details["language"] = lang
    details["movie_bio"] = movie_bio
    details["runtime"] = runtime_of_movie
    details["movie_genre"] = gen
    with open ("movie_details.json","w") as movie:
        json.dump(details,movie,indent=4)
    return(details)
scrape_movie_details()
                