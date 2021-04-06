from Task1 import scrape_top_list
import requests
import json
from bs4 import BeautifulSoup 
from pprint import pprint

name1=scrape_top_list()

realsing_year = []
unique_year = []
def group_by_year ():
    i = 0
    while i <len(name1):
        year = name1[i]["year"]
        realsing_year.append(year)
        i = i +1
    j = 0
    while j <len(realsing_year):
        if realsing_year[j] not in unique_year:
            unique_year.append(realsing_year[j])
        j = j+1
    k = 0
    while k < len(unique_year):
        l = 0
        while l < len(unique_year):
          if unique_year[k] < unique_year[l]:
            a = unique_year[k]
            b = unique_year[l]
            unique_year[k] = b
            unique_year[l] = a
          l = l + 1
        k = k + 1 
    my_dict = {}
    a = 0
    while a < len(unique_year):
        list1 = []
        b = 0
        while b < len(name1):
            if unique_year[a] == name1[b]["year"]:
                if name1[b] not in list1:
                    list1.append(name1[b])
            b = b + 1
        my_dict[unique_year[a]] = list1 
        a = a + 1
    with open ("year_vise_movies.json","w") as sara_data2:
        json.dump(my_dict,sara_data2,indent = 4)
    return(my_dict)
group_by_year()