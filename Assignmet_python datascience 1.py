#!/usr/bin/env python
# coding: utf-8

# Q1. What is Abstraction in OOps? Explain with an example.

# Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user. This is one of the core concepts of object-oriented programming (OOP) languages. 

# In[1]:


from abc import ABC, abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")   
          
# Driver code   
t= Tesla ()   
t.mileage()   
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage()  


# Q2.What is abc module in python? Why is it used?

# The 'abc' module in Python library provides the infrastructure for defining custom abstract base classes.
# 
# 'abc' works by marking methods of the base class as abstract. This is done by @absttractmethod decorator.

# Q3. How can we achieve data abstraction?

# abstraction can be achieved by having/using abstract classes and methods in our programs

# In[ ]:





# In[ ]:




