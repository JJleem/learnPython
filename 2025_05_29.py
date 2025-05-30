# /// 파이썬 라이브러리 사용 
from random import randint

"""
# // 랜덤한 숫자 생성
"""
# user_choice =int(input("Choose number."))
# pc_choice = randint(1,50) # I imported randint from random module to generate a random number between 1 and 50



# if user_choice == pc_choice:
#     print("y  ou win")
# elif user_choice < pc_choice:
#     print("higher Computer choice is", pc_choice)
# elif user_choice > pc_choice:
#     print("lower Computer choice is", pc_choice)

# if True :
#     print("HI Im Ture")


# while 문은 if 와같지만 멈추지않음 if는 한번 while 은 동안 반복됨
""""
distance = 0

while distance < 20:
    print("Im running", distance, "km")
    distance = distance + 1  # distance += 1  # distance = distance + 1
"""



# print("welcom to python casino")

# pc_choice = randint(1,50) # I imported randint from random module to generate a random number between 1 and 50

# playing = True
# while playing:
#   user_choice = int(input("Choose a number between 1 and 50: "))
#   if user_choice == pc_choice:
#     print("you win")
#     playing = False
#   elif user_choice < pc_choice:
#     print("higher Computer choice is", pc_choice)
#   elif user_choice > pc_choice:
#     print("lower Computer choice is", pc_choice)

# data structures
# 
# 
# list

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]



days_of_week.remove("Monday")  # remove Monday from the list
days_of_week.count("Tuesday")  # count how many times Tuesday appears in the list
days_of_week.clear()  # clear the list
days_of_week.append("Monday")  # add Monday back to the list
print(days_of_week)


# name = "nico"

# print(name.replace("n", "m"))  # replace n with m