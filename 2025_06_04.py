#class
class Dog:
      def __init__(self, name,breed):
        self.name = name
        self.age = 13
        self.breed = breed


class Puppy(Dog):
    # def __init__(self, name,breed):
    #     self.name = name
    #     self.age = 13
    #     self.breed = breed
    def __str__(self):
        return f"Puppy(name={self.name}, age={self.age}, breed={self.breed})"

    def woof_woof(self):
        print("멍멍!")
    # def introduce(self):
    #     self.woof_woof()
    #     print(f"안녕하세요, 제 이름은 {self.name}이고, 나이는 {self.age}살이며, 품종은 {self.breed}입니다.")
    #     self.woof_woof()
    




# print(f"Name: {ruffles.name}, Age: {ruffles.age}, Bread: {ruffles.breed}")
# print(f"Name: {bibi.name}, Age: {bibi.age}, Bread: {bibi.breed}")
# print(ruffles,bibi)
# print(ruffles.introduce())
# Puppy 클래스에 introduce 메서드를 추가하여 객체의 정보를 출력하는 기능을 구현
class GuardDog(Dog):
    

    # def __init__(self,name,breed):
    #     self.name = name
    #     self.breed = breed
    #     self.age = 5

    def grrr(self):
        print("으르렁!")




ruffles = GuardDog(name="samdol",breed="yorkshire")
# ruffles = Puppy("Ruffles", "Beagle")
bibi = Puppy(name="vinchi",breed="turtle")
print(ruffles.grrr(), ruffles.name, ruffles.breed, ruffles.age)