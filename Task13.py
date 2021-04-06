import requests
from Task12 import scrape_movie_cast
import json
from pprint import pprint
from bs4 import BeautifulSoup
list1 = scrape_movie_cast()
def scrape_movie_details():
    imdb_api = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
    imdb_url = requests.get(imdb_api)
    Text_Data = imdb_url.json
    soup = BeautifulSoup(imdb_url.text,"html.parser")
    my_dict = {}
    name1 = []
    lang = []
    dire = []
    gen = []
    div = soup.find("div", class_="lister")
    body = div.find("tbody", class_="lister-list")
    name = body.find_all("tr")
    tr = name[10]
    movies_name = tr.find("td",class_ = "titleColumn").a.get_text()
    years = tr.find("td",class_ = "titleColumn").span.get_text()
    link = tr.find("td",class_= "titleColumn").a['href']
    url = 'https://www.imdb.com' + str(link)
    rating = float(tr.find("td",class_="ratingColumn imdbRating").strong.get_text())
    movie_url = requests.get(url)
    soup = BeautifulSoup(movie_url.text,"html.parser")
    director_name = soup.find("div",class_="credit_summary_item").a.get_text()
    dire.append(director_name)
    for_poster  = soup.find("div",class_="poster").a['href']
    movie_poster = "https://www.imdb.com/" + for_poster
    bio = soup.find("div", class_="plot_summary" )
    movie_bio = bio.find("div", class_="summary_text").get_text().strip()
    div1 = soup.find("div",attrs={"class":"article","id":"titleDetails"})
    more_detail = div1.find_all("div")
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
    movie_genre = time.find_all("a")
    movie_genre.pop()
    for i in movie_genre:
        genre = i.get_text()
        gen.append(genre)
    my_dict["name"] = movies_name
    my_dict["year"] = int(years[1:5])
    my_dict["rank"] = rating
    my_dict["movie url"] = url
    my_dict["country"] = "India"
    my_dict["language"] = lang
    my_dict["director"] = dire
    my_dict["movie bio"] = movie_bio
    my_dict["poster url"] = movie_poster
    my_dict["cast"] = list1
    my_dict["runtime"] = runtime_of_movie
    my_dict["genre"] = gen
    with open("scrape_movie.json","w") as data:
        json.dump(my_dict,data,indent=4)
    return(my_dict)
scrape_movie_details()

