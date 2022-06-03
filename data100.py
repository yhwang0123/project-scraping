from bs4 import BeautifulSoup
import requests
import csv
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# open txt file and get the link
f = open("immo_urls.txt")
urls = [url.strip() for url in f.readlines()]  # remove lines in urls
urls_100 = urls[:100]  # to get the first 100 links for test


# set empty list to save headings and data
headings = []
data = []


# creat a function to get all the data we need for properties:
def get_property_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    search_id = str(url).split("?")[0].split("/")[-1]
    postcode = str(url).split("?")[0].split("/")[-2]
    # Make an execption for any error may happen
    try:
        property_type = (
            soup.find("h1", class_="classified__title").text.strip().split("\n")[0]
        )
    except Exception as e:
        print("property_type not available")
        property_type = None
        pass

    # the data in the table
    tables = soup.find_all("table", class_="classified-table")
    for table in tables:
        for th in table.find_all("th"):
            headings.append(th.contents[0].strip())

        for td in table.find_all("td"):
            data.append(td.contents[0].strip())

    new_dict = dict(zip(headings, data))
    updict = {
        "search_id": search_id,
        "type of propery": property_type,
        "Postcode": postcode,
        "Link": url,
    }
    updict.update(new_dict)
    return updict


# creat a function to save the data results
def save_csv(results):
    # create a dataframe
    df = pd.DataFrame(results)
    # export DataFrame to CSV file
    df.to_csv("property_100.csv", index=False, sep=";")


# as there are multiple dictionary, I will save them in a list
results = []
for url in urls_100:
    results.append(get_property_data(url))
print("Total results:", len(results))  # get to know how many properties data we had got
save_csv(results)  # call the function for saving results
