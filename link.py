# in link.py, I will find all the link for sale of apartment and house on immoweb
# the link will be saved into a txt file

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# I use selenium to find the links, as beautifulsoup can't extract the link information I want
# the number of properties for sale on immoweb are 61552
# as our goal is just get minimum 10000 property data, I try to get information of first 300 search pages
page_numbers = list(range(301))[1:301]

# list to store all the links of properties
urls_list = []

# for loop for all 100 search pages

for page_number in page_numbers:
    # I use ChromeDriverManager as Chrome executable_path because the path doesn't work for me
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&page={page_number}&orderBy=relevance"
    driver.get(url)

    links = driver.find_elements(by=By.XPATH, value="//a[@class='card__title-link']")
    for link in links:
        with open("immo_urls.txt", "a") as f:  # save the links in txt file
            f.write(link.get_attribute("href") + "\n")
    driver.quit()
