from abc import ABC, abstractmethod

class Great(ABC):
    @abstractmethod
    def say_hello(self):
        pass#Abstract method
class English(Great):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())

#crate file = x
#read = r 
#a = appned
#write= w