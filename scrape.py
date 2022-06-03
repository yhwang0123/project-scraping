from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint
from csv import writer
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

f = open("immo_urls.txt")
urls = [url.strip() for url in f.readlines()]  # remove lines in urls

for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    property_type = (
        soup.find("h1", class_="classified__title").text.strip().split("\n")[0])
    print(property_type)
    # print("----------------")


# write all the data in the dictionary to a csv file
"""immo_file = open("immo.csv", "w")
a_dict = {"a": 1, "b": 2}
writer = csv.writer(immo_file)
for key, value in a_dict. items():
writer.writerow([key, value])
immo_file. close()"""
