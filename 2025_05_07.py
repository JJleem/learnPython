# print("Hello, World!")

# def say_hello(user_name):
#   print("hellow how", user_name, " how r u?")


# say_hello("jaejun")

# def say_hello(user_name="anonymous"):
#     print("Hello, how are you, " + user_name + "?")

# say_hello("Jaejun")
# say_hello()

my_age = 20
my_name= "Jaejun"

f"Hello, my name is {my_name} and I am {my_age} years old."
def say_hello(user_name="anonymous", age=0):
    print(f"Hello, how are you, {user_name}? You are {age} years old.")

say_hello(my_name, my_age)

def make_juice(fruite):
    return f"{fruite} + juice"

def add_ice(juice):
    return f"{juice} + ice"

def add_sugar(iced_juice):
    
    return f"{iced_juice} + sugar"

juice = make_juice("kiwi")

cold_juice = add_ice(juice)

sweet_cold_juice = add_sugar(cold_juice)

print(sweet_cold_juice)

