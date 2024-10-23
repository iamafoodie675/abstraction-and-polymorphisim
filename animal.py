from abc import ABC,abstractmethod

class Animal(ABC):
    def move(self):
        pass
    
class Human(Animal):
    def move(self):
        print("i can walk and run")
        
class Snake(Animal):
    def move(self):
        print("i can crawl")
        
class Dog(Animal):
    def move(self):
        print("i can bark")
        
class Lion(Animal):
    def move(self):
        print("i can roar")
        
        
R =Human()
R.move()
R =Snake()
R.move()
R =Dog()
R.move()
R =Lion()
R.move()
