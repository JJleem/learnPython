import requests
from bs4 import BeautifulSoup
import cloudscraper


url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

scraper = cloudscraper.create_scraper()  # Cloudflare 우회용
response = scraper.get(url)

print(f"응답 코드: {response.status_code}")


soup = BeautifulSoup(response.text, 'html.parser')
jobs = soup.find("section", class_="jobs").find_all("li")


if jobs:
    print(jobs)
else:
    print("❌ 'jobs' 클래스 찾을 수 없음")

    ### 0610 우회하여 li 태그 찾기까지함 