from abc import ABC, abstractmethod

class hiddenClass(ABC):
    def print(self,x):
        print("passed value: ",x)
        
        
    @abstractmethod
    def task(self):
        print("We are inside ABsclass task")
        
        
class testClass(hiddenClass):
    
    def task(self):
        print("We are inside test_class task")
        
        
ob1 =testClass()
ob1.task()
ob1.print(100)

hidden =hiddenClass()
hidden.task()
        