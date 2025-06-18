from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv
p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")
# time.sleep(5)

# page.click("button.Aside_searchButton__Ib5Dn")

# time.sleep(5)

# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
# # page.screenshot(path="./screenshot/screenshot.png")

# time.sleep(5)

# page.keyboard.down("Enter")

# time.sleep(5)


# page.click("a#search_tab_position")

for x in range(5):
  time.sleep(3)
  page.keyboard.down("End")

time.sleep(5)

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs_db = []
jobs = soup.find_all("div", class_="JobCard_container__zQcZs")

for job in jobs:
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong",class_="JobCard_title___kfvj").text
    company_name= job.find("span", class_="JobCard_companyName__kmtE0").text
    reward = job.find("span", class_="JobCard_reward__oCSIQ").text
    job = {
    "link": link,
    "title": title,
    "company_name": company_name,
    "reward": reward
    }
    jobs_db.append(job)


file = open("jobs.csv","w",encoding='utf-8', newline='')
writter = csv.writer(file)
writter.writerow(["Title","Company","Location","Reward","Link"])
for job in jobs_db:
   writter.writerow(job.values())

# print(jobs_db)
# print(len(jobs_db))
# def plus (a,b):
#     return a + b

# plus(1,2)