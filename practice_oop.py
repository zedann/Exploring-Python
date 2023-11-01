from datetime import date
# class Student:
#     #class attr | can i say it is static ?
#     no_of_students = 0
#     def __init__(self , name , age , courses=[]):
#         # private attr __ | protected _ 
#         self.__name = name
#         # instance attr
#         self.age = age
#         self.courses = courses
#         Student.no_of_students += 1
#     # class method
#     @classmethod
#     def init_from_birth_year(cls , name , birth_year):
#         return cls(name , date.today().year -  birth_year)
#     # encabsulation 'but i do not agree that it just getters and setters 
#     def getName(self):
#         return self.__name
#     def setName(self , newName):
#         self.__name = newName
#     # methods
#     def introduce(self):
#         print(f'my name is {self.__name} and my age is {self.age}')
#     def is_old(self , compAge):
#         return self.age > compAge 
    
# # std3 = Student.init_from_birth_year("zedan" , 2003)
# # std3.introduce()
# # ------------------------------------------------
# # std1 = Student('zedan' , 20 , ['cs','logic'])
# # std2 = Student('ahmed' , 24 , ['cs','logic'])
# # # print(std1 , std2)
# # print(Student.no_of_students , std1.no_of_students)
# # std1.introduce()
# # print(std1.is_old(30))
# # some basic stuff 
# std1 = Student('zedan',20 , ['cs' , 'logic'])
# std2 = Student('ahmed' , 24 , ['cs','logic'])
# # std1.grade = 90
# # print(std1.grade)
# # print(std2.grade)
# # print(std1.__name)

# class Math:
#     @staticmethod
#     def add(x , y):
#         return x + y
#     @staticmethod
#     def max(x,y):
#         return max(x,y)
#     @staticmethod
#     def PI():
#         return 3.14

# class Pizza:
#     def __init__(self,radius , ingredients) -> None:
#         self.radius = radius
#         self.ingredients = ingredients
#     # dunder method
#     def __str__(self):
#         return f'Pizza ingredients are {self.ingredients}'
#     @staticmethod
#     def circle_area(r):
#         return Math.PI() * (r**2)

        
class Person:
    def __init__(self , name , age) -> None:
          self.name = name
          self.age = age
    def display(self):
        return f'name is {self.name} and age is {self.age}'
    
class Man(Person):
    # class attr
    gender='Male'
    no_of_men = 0
    def __init__(self , name , age , voice):
        super().__init__(name , age)
        self.voice = voice
        Man.no_of_men += 1
    # polymorphism
    def display(self):
       return super().display() + f' and voice is {self.voice} and gender is {self.gender}'

class Woman(Person):
    gender = 'Female'
    no_of_women = 0
    
    def __init__(self, name, age , hair) -> None:
        super().__init__(name, age)
        self.hair = hair
        Woman.no_of_women += 1
    def display(self):
        return super().display() + f' and woman stuff (" '
    
# man1 = Man('Zedan' , 20 , 'high')
# man2 = Man('Ahmed' , 21 , 'Mediam')
# print(man1.display())
# woman1 = Woman('Sara' , 25 , 'curly')
# print(woman1.display())

# abstraction 
from abc import ABC , abstractmethod

class Shape:
    def __init__(self) -> None:
        pass
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def circum(self):
        pass
class Square(Shape):
    def __init__(self , side) -> None:
        self.__side = side
    def area(self):
        return self.__side ** 2
    def circum(self):
        return self.__side * 4
    
class Rect(Shape):
    def __init__(self , height , width) -> None:
        self.__height = height
        self.__width = width
    def area(self):
        return self.__width * self.__height
    def circum(self):
        return 2*(self.__width + self.__height)

