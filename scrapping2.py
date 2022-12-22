from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("C:\\Users\\Rajnish prabhakar\\Downloads\\C141_SA_BP-main\\C141_SA_BP-main\\chromedriver.exe")

import requests
page = requests.get(START_URL)
soup = BeautifulSoup(page.text, "html.parser")
star_table = soup.find("table")
tem_list = []

table_rows = star_table.find_all("tr")
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    tem_list.append(row)

name_of_stars = []
distance = []
mass = []
radius = []


for i in range(1, len(tem_list)):
    name_of_stars.append(tem_list[i] [0])
    distance.append(tem_list[i] [5])
    mass.append(tem_list[i] [7])
    radius.append(tem_list[i] [8])


headers = ["name_of_stars", "distance", "mass", "radius" ]

stars = pd.DataFrame(list(zip(name_of_stars, distance, mass, radius)), columns = headers)
stars.to_csv("stars2.csv")