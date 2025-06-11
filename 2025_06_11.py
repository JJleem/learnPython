# import requests
# from bs4 import BeautifulSoup
# import cloudscraper


# url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

# scraper = cloudscraper.create_scraper()  # Cloudflare 우회용
# response = scraper.get(url)

# # print(f"응답 코드: {response.status_code}")


# soup = BeautifulSoup(response.text, 'html.parser')
# jobs = soup.find("section", class_="jobs").find_all("li")[0:-1]  # 마지막 li 태그는 광고이므로 제외


# # if jobs:
#     # print(jobs)
# # else:
# #     print("❌ 'jobs' 클래스 찾을 수 없음")

#     ### 0610 우회하여 li 태그 찾기까지함 
#     ### 0611 li 태그에서 제목과 지역 추출하기
# for job in jobs:
#     # title = job.find("h4", class_="new-listing__header__title").text
#     # region= job.find("p", class_="new-listing__company-headquarters").text
#     features = job.find_all("p", class_="new-listing__categories__category")
#     feature , time, top,money,position = features.find_all("p", class_="new-listing__categories__category")
#     feature = feature.text
#     top = top.text 
#     time = time.text
#     money = money.text
#     position = position.text
#     print(f"특징: {feature} top: {top} | 시간: {time} | 급여: {money} | 위치: {position}")
#     # print(f"{categories}")
#     # print(f"제목: {title}, 지역: {region}")
    


# import requests
# from bs4 import BeautifulSoup
# import cloudscraper

# url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"
# scraper = cloudscraper.create_scraper()
# response = scraper.get(url)

# soup = BeautifulSoup(response.text, 'html.parser')
# jobs = soup.find("section", class_="jobs").find_all("li")[0:-1]  # 마지막 광고 제외

# for job in jobs:
#     title_tag = job.find("h4", class_="new-listing__header__title")
#     company_tag = job.find("p", class_="new-listing__company-name")
#     region_tag = job.find("p", class_="new-listing__company-headquarters")

#     title = title_tag.text.strip() if title_tag else "N/A"
#     company = company_tag.text.strip() if company_tag else "N/A"
#     region = region_tag.text.strip() if region_tag else "N/A"

#     categories = job.find_all("p", class_="new-listing__categories__category")
#     extracted = [c.text.strip() for c in categories]

#     # 값이 없을 수 있으니 개수 확인해서 할당
#     feature = extracted[0] if len(extracted) > 0 else "N/A"
#     top     = extracted[1] if len(extracted) > 1 else "N/A"
#     time    = extracted[2] if len(extracted) > 2 else "N/A"
#     money   = extracted[3] if len(extracted) > 3 else "N/A"
#     position= extracted[4] if len(extracted) > 4 else "N/A"

#     print(f"회사: {company} | 제목: {title} | 위치: {region}")
#     print(f"특징: {feature} | Top: {top} | 시간: {time} | 급여: {money} | 포지션: {position}")
#     print("-" * 80)


import requests
from bs4 import BeautifulSoup
import cloudscraper

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"
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
