import requests
from bs4 import BeautifulSoup
import cloudscraper

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"


def scrape_page(url):
    print(f"Scraping URL: {url}...")
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find("section", class_="jobs").find_all("li")[0:-1]  # 마지막 광고 제외

    for job in jobs:
      title_tag = job.find("h4", class_="new-listing__header__title")
      company_tag = job.find("p", class_="new-listing__company-name")
      region_tag = job.find("p", class_="new-listing__company-headquarters")


      title = title_tag.text.strip() if title_tag else "N/A"
      company = company_tag.text.strip() if company_tag else "N/A"
      region = region_tag.text.strip() if region_tag else "N/A"

    # 초기값 설정
      feature = top = time = money = position = "N/A"

      categories = job.find_all("p", class_="new-listing__categories__category")

      for cat in categories:
        class_list = cat.get("class", [])
        text = cat.text.strip()
        if "new-listing__categories__category--featured" in class_list:
            feature = text
        elif "new-listing__categories__category--top-company" in class_list:
            top = text
        elif time == "N/A":
            time = text
        elif money == "N/A":
            money = text
        elif position == "N/A":
            position = text
        print(f"회사: {company} | 제목: {title} | 위치: {region}")
        print(f"✔️ 특징: {feature} | 🏢 Top: {top} | 🕒 시간: {time} | 💰 급여: {money} | 📍 포지션: {position}")
        print("-" * 80)

    


scraper = cloudscraper.create_scraper()
response = scraper.get("https://weworkremotely.com/remote-full-time-jobs?page=1")

soup = BeautifulSoup(response.content, 'html.parser')
buttons = len(soup.find("div", class_="pagination").find_all("span", class_="page"))

for x in range(buttons):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape_page(url)

