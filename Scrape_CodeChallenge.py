import requests
from bs4 import BeautifulSoup
import cloudscraper

keywords = [
  "flutter",
  "python",
  "golang"
]

r= requests.get("https://remoteok.com/remote-flutter-jobs", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"})

soup = BeautifulSoup(r.content, 'html.parser')
jobs = soup.find_all("tr", class_="job")
for job in jobs:
    title_tag = job.find("h2", itemprop="title")
    company_tag = job.find("h3", itemprop="name")
    region_tag = job.find("div", class_="location")

    title = title_tag.text.strip() if title_tag else "N/A"
    company = company_tag.text.strip() if company_tag else "N/A"
    region = region_tag.text.strip() if region_tag else "N/A"

    print(f"회사: {company} | 제목: {title} | 위치: {region}")


