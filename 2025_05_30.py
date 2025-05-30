"""
# 튜플 ( 불변성 , 순서가 있는 자료형 )
# 튜플은 변경할 수 없는 리스트
# 튜플은 소괄호로 묶어서 표현
# .함수 index,count 정도밖에없음
# index -1 부터도 가능 ( -1, -2, -3 ... )

# 수정해야하는 데이터? List , # 수정하지 않는 데이터? Tuple
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")


#딕셔너리 객체
# 딕셔너리는 키와 값의 쌍으로 이루어진 자료형
# 키는 중복될 수 없고, 값은 중복될 수 있음
player = {
    "name": "John",
    "age": 30,
    "team": "Red",
    "position": "Forward",
    "fav_food": ["Pizza", "Burger", "Pasta"]
}
# 딕셔너리에서 키를 사용하여 값에 접근
print(player["name"])  # John

player.get("age")  # 30
# 딕셔너리에 새로운 키-값 쌍 추가
player["score"] = 100
# 딕셔너리에서 키-값 쌍 삭제
del player["team"]
# 딕셔너리의 모든 키-값 쌍 출력
for key, value in player.items():
    print(f"{key}: {value}")
# 딕셔너리의 키 목록 출력
print(player.keys())  # dict_keys(['name', 'age', 'position', 'fav_food', 'score'])
# 딕셔너리의 값 목록 출력
print(player.values())  # dict_values(['John', 30, 'Forward', ['Pizza', 'Burger', 'Pasta'], 100])
# 딕셔너리의 키-값 쌍 목록 출력
print(player.items())  # dict_items([('name', 'John'), ('age', 30), ('position', 'Forward'), ('fav_food', ['Pizza', 'Burger', 'Pasta']), ('score', 100)])
# 딕셔너리의 길이 출력
print(len(player))  # 5
# 딕셔너리의 특정 키가 존재하는지 확인
print("name" in player)  # True
# 딕셔너리의 특정 키가 존재하지 않는지 확인 
player["fav_food"].append("Sushi")  # 리스트에 새로운 음식 추가
"""
#for loop 문

#requests 모듈을 사용하여 웹사이트의 상태 코드 확인

from requests import get

websites = (
    "www.google.com",
    "www.youtube.com",
    "www.facebook.com",
    "www.instagram.com",
    "www.twitter.com"
)
for website in websites:
    if not website.startswith("https://"):
       website = f"https://{website}"  # Replace "http://" with "https://"
       response = get(website)
       print(f"Updated website: {website}")
       print(f"Status code: {response.status_code}")
    else:
        # If it does not start with "https://", print a warning
      print(f"Warning: {website} does not use a secure connection.")



# for loop with range
for i in range(5):
    print(f"Number: {i}")







