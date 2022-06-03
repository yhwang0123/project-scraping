# in this file, I will scraping the real estate informaiton on one page, just for a test
# I choose one page from immoweb, which is Belgium's leading property website

# install and import the necessary library to do the scraping
from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint
import pandas as pd

# test page as below, it's a house in Herzele, get the page
url = "https://www.immoweb.be/en/classified/penthouse/for-sale/sint-niklaas/9100/9942698?searchId=62986b673d850"
page = requests.get(url)

# creat soup to save the html content of this page
soup = BeautifulSoup(page.content, "html.parser")

# use beautifulsoup to find type of property
property_type = soup.find("h1", class_="classified__title").text.strip().split("\n")[0]
print(property_type)
print("----------------")

# find postcode and search_id from url
postcode = str(url).split("?")[0].split("/")[-2]
print(postcode)
print("----------------")
search_id = str(url).split("?")[0].split("/")[-1]
print(search_id)
print("----------------")

# As other information are saved in different tables, I try to find all of them using tag 'table'
tables = soup.find_all("table", class_="classified-table")

# create empty lists to keep headings and data
headings = []
data = []

for table in tables:
    for th in table.find_all("th"):
        headings.append(th.contents[0].strip())

    for td in table.find_all("td"):
        data.append(td.contents[0].strip())


# build up a dictionary to save the table data
new_dict = dict(zip(headings, data))
# add key and value of search_id, property_type, price postcode and link
# in the beginning of the dictionary
updict = {
    "search_id": search_id,
    "type of propery": property_type,
    "Postcode": postcode,
    "Link": url,
}

updict.update(new_dict)
print(updict)
