from Task1 import scrape_top_list
import requests
import json
from bs4 import BeautifulSoup 
from pprint import pprint
name1=scrape_top_list()
year = []
def group_by_decade():
    i = 0 
    while i < len(name1):
       year.append(name1[i]["year"])
       i = i + 1
    year.sort()
    j = 0
    my_dict = {}
    while j < len(year):
        dec = (year[j]//10)*10
        k = 0
        decade = []
        while k < len(name1):
            if name1[k]["year"] >= dec and name1[k]["year"] < (dec + 10):
                decade.append(name1[k])
            my_dict[dec] = decade
            k = k + 1
        j = j + 1
        with open("decade_vise_movie.json","w") as saral_data3:
            json.dump(my_dict,saral_data3,indent = 4)
group_by_decade()








     



