from bs4 import BeautifulSoup
import requests
import re
import pandas as pd 
import time
import undetected_chromedriver as uc




site = "http://webcache.googleusercontent.com/search?q=cache:https://clutch.co/us/agencies/digital-marketing?page="
# site = "https://clutch.co/us/agencies/digital-marketing?page="
number_of_pages_to_be_scraped = 520



company_name = []
website = []
ser_foc = []
country = "United States"

for i in range(number_of_pages_to_be_scraped):
    _page = site + str(i+1)
    req=requests.get(_page)
    content=req.text
    soup=BeautifulSoup(content)

    a = soup.find_all("a", {"class": "company_title directory_profile"})
    website_address = soup.find_all("a", {"class": "website-link__item"})
    service_focus = soup.find_all("div", {"class": "chart-label hidden-xs"})

    for a_tags in a:
        company_name.append(a_tags.text.strip())

    for address in website_address:
        website.append(address['href'])
        
    for focus in service_focus:
        ser_foc.append(focus.text.strip())

    print(str(i) + ": response status code" + str(req.status_code))
    print("\n")
    time.sleep(5)
    
# print(len(company_name))
# print(len(website_address))
# print(len(ser_foc))

df = pd.DataFrame(list(zip(company_name, website, ser_foc)), columns=["Company name", "Website", "Service focus."])
df.to_csv('data.csv', index=False)
