

"""
from requests import get

websites = (
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://www.instagram.com",
    "https://www.twitter.com",
    "https://d2av2ea630m6st.cloudfront.net",
)

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    
    try:
        response = get(website)
        status_code = response.status_code

        if status_code == 200:
            results[website] = f"OK: {status_code}"
        elif 300 <= status_code < 400:
            results[website] = f"Redirect: {status_code}"
        else:
            results[website] = f"Failed: {status_code}"
    except Exception as e:
        results[website] = f"Error: {e}"

# 최종 결과 출력
print(results) 
"""

# OOP 객체지향 프로그래밍
# 클래스와 객체를 사용하여 OOP 개념을 구현

jaejun = {
    "name": "Jaejun",
    "XP": 1500,
    "team": "MC",
}

def created_player(name,xp,team):
    return {
    "name": name,
    "xp": xp,
    "team": team,
    }
    
def introduct_player(player):
    name= player[name]
    xp = player["XP"]
    team = player["team"]
    print(f"Player Name: {name}, XP: {xp}, Team: {team}")

jaejun = created_player("Jaejun", 1500, "MC")

introduct_player(jaejun)