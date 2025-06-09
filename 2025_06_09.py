#class
class Dog:
      def __init__(self, name,breed,age):
        self.name = name
        self.age = age
        self.breed = breed


class Puppy(Dog):
    def __init__(self, name,breed):
       super().__init__(
           name=name,
            age=1,  # 기본값으로 1살로 설정
           breed=breed,
          
       )
       self.spoiled = True  # 기본값으로 True로 설정
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
    def __init__(self, name, breed):
        super().__init__(name=name, age=5, breed=breed)
        self.aggresive = True
   

    def grrr(self):
        print("으르렁!")




ruffles = GuardDog(name="samdol",breed="yorkshire")
# ruffles = Puppy("Ruffles", "Beagle")
bibi = Puppy(name="vinchi",breed="turtle")
print(ruffles.grrr(), ruffles.name, ruffles.breed, ruffles.age)

# class함수와 method 차이점