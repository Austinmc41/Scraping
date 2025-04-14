from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd


EMPLOYER = 'EmployerProfile_profileContainer__63w3R EmployerProfile_compact__28h9t'

l=list()
o={}

# setup for using chromium executable
PATH='/Users/austin/Desktop/Scraping/chromedriver-mac-arm64/chromedriver'
options = webdriver.ChromeOptions()
service = Service(executable_path=PATH)

# target url for scraping
target_url = "https://www.glassdoor.com/Job/new-york-python-jobs-SRCH_IL.0,8_IC1132348_KO9,15.htm?clickSource=searchBox"

# selenium oepn chrome allow to stay open for long enough to get page source close chrome page
driver=webdriver.Chrome(service=service, options=options)
driver.get(target_url)
driver.maximize_window()
time.sleep(2)
resp = driver.page_source
driver.close()

soup=BeautifulSoup(resp,'lxml')

allJobsContainer = soup.find("ul", class_='JobsList_jobsList__lqjTr')

allJobs = allJobsContainer.find_all("li")


for job in allJobs:
    try:
        o["name-of-company"] = job.find("span", class_="EmployerProfile_compactEmployerName__9MGcV").get_text(strip=True)
    except:
        o["name-of-company"] = None

    try:
        o["name-of-job"] = job.find("a", class_="JobCard_jobTitle__GLyJ1").get_text(strip=True)
    except:
        o["name-of-job"] = None

    try:
        o["location"] = job.find("div", class_="JobCard_location__Ds1fM").get_text(strip=True)
    except:
        o["location"] = None

    try:
        salary_tag = job.find("div", class_="JobCard_salaryEstimate__QpbTW")
        o["salary"] = salary_tag.get_text(strip=True) if salary_tag else None
    except:
        o["salary"] = None

    l.append(o)
    o = {}

df = pd.DataFrame(l)
df.to_csv('jobs.csv', index=False, encoding='utf-8')





