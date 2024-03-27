"""
Below is an example of abstract method
Here if we remove the abstract method decorator, we will be able to create the object
since the abstract method, object cannot be created, we need to use the decorator and extend
with ABC.
"""

from abc import ABC, abstractmethod


class Test(ABC):

    @abstractmethod
    def testing(self):
        pass


# a1 = Test()

class Baselcass(Test):

    def __init__(self):
        print("Constructor Called")

    def testing(self):
        print("This is calling from Baseclass")


b1 = Baselcass()

"""
If we dont override the abstract method we will get below error.so overide it
TypeError: Can't instantiate abstract class Baselcass with abstract method testing  
"""
