# in this file, I will get data of all the 10000+ links
# I will use concurrency to speed it up
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import concurrent.futures  # to speed up the scraping

f = open("immo_urls.txt")
urls = [url.strip() for url in f.readlines()]  # remove lines in urls


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
    try:
        price = soup.find("p", class_="classified__price").text.strip().split(" ")[0]
    except Exception as e:
        print("price not available")
        price = None
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
        "Property price": price,
        "Postcode": postcode,
        "Link": url,
    }
    updict.update(new_dict)
    return updict


# to speed up the scraping using concurrent
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(get_property_data, urls)


def save_csv(results):
    # create a dataframe
    df = pd.DataFrame(results)
    # export DataFrame to CSV file
    df.to_csv("final_data.csv", index=False)


results = []
for url in urls:
    results.append(get_property_data(url))
print("Total results:", len(results))
save_csv(results)
