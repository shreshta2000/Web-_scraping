from Task5 import top_movie_list
import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup

list1 = top_movie_list
Genre = []
my_dict = {}
def analyse_movies_genre():
    for j in list1:
        for i in j["movie_genre"]:
            Genre.append(i)
    for k in Genre:
        if k not in my_dict:
            my_dict[k] = 1
        else:
            my_dict[k] = 1+1
    with open("genre.json","w") as lan:
        json.dump(my_dict,lan,indent=4)
    return(my_dict)
analyse_movies_genre()
