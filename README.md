1. Description
In this project, I scraped real propety information from immoweb, a leading property website in Belgium.
My goal is to get minimal 10 000 inputs for all of Belgium.


2.Installation
-beautifulsoup4
-requests
-selenium
-ChromeDriverManager

3.Files in this repo
test.py - for testing scraping for one property link

link.py - get all the 10000+ links

immo_urls.txt - all the links

data100.py - code for scraping 100 links

property_100.csv - data for the first 100 properties

data10000.py - code for scraping on 10000+ links

final_data.csv - data for all the 10000+ properties

cleaned_data.py - clean data for 100 properties

4.Timeline
This is a three-day project. So I split my work into small pieces and do it each day.

Day 1. Parse on first test page

Day 2. Get all the link of 10000+

Day 3. Scarping test for first 10 pages

       Get data for 10000+ pages(not finished, process slow)
       
       Clean all the codes and write README file

5. Strategy
#Firstly, before I began to work on this project, I review what I have learned in previous material about web scraping and I have read more tutorials around this topic, which has prepared me for the projects. 

#Second, I think about the step I should do for this projects.
First, I should be able to parse one property page. I look deeply through one page, and try to find the information we need. I found that the Immo page use a table to save some of the data. So I decided to use dictionary to get the data in table. But for some information like price, post code, and property table, they are not in the table. So I need to get them separately from html text.

#Thirdly, I planned to get all the links of properties for sale, it has 333 page total. I use loop to go through all the pages. But the difficulties I met is I intend to use beautiful soup to get all the links. But after several trials, it didn’t work. So I changed to use selenium to scrape the links. But the chrome driver path seems to have some problem, I googled it and tried to fix it. But no success. So I installed ChromeDriverManager instead and it run well. Finally I got all the links I want.

Next, I scraped with first 100 pages. I use the code in test.py file and add exception for some codes in case there may be some error as there is no such data avaiable. With 100 pages, I got the csv file. Then I tried with 10000+ file, and I tried to use the concurrency to speed the scraping process. But it still takes longer than I expected. So I worked on clean data on 100 pages.

Special thanks to Louis and my colleagues for their great help during this project. Louis encouraged us a lot. When I met with some problems, he didn’t give direct solution, but he inspired us, let us try by ourselves. I really appreciate his kind support. Also my colleagues in the same tables, Pragati, Yuri and Jorg, supported me in different ways. We helped each other. It was a good learning atmosphere.
