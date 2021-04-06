from Task5 import top_movie_list
import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup
list1 = top_movie_list
director = []
my_dict = {}
def analyse_movies_directors ():
    for i in list1:
        for j in i["director"]:
            director.append(j)
        for k in director:
            if k not in my_dict:
                my_dict[k] = 1
            else:
                my_dict[k] = 1 + 1
    with open("movies_director.json","w") as lan:
        json.dump(my_dict,lan,indent=4)
    return(my_dict)
analyse_movies_directors ()

