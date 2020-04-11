# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:39:42 2019

@author: Abhishek
"""

class MyObject:
    def __init__(self,name,surname,year_of_birth):
        self._name = name
        self._surname = surname
        self._year_of_birth = year_of_birth
    
    def age(self, current_year):
        return current_year - self._year_of_birth
    
    def __str__(self):
        return "%s %s born in %d" %(self._name, self._surname, self._year_of_birth)
    

#Person = MyObject("Abhishek", "Trivedi",1996)
#print(Person.age(2019))
#print(Person)
#print(Person.__dict__.keys())
        
    
class Inherit(MyObject):
    def __init__(self, id, *args, **kargs):
        super(Inherit, self).__init__(*args, **kargs)
        self._id = id

    def __str__(self):
        return super(Inherit, self).__str__() + " and had ID : %d"%(self._id)
#Second = Inherit(2, "XYZ", "FRG", 1994)

#print(Second)


######## A whole new Program ########
        
class Tyres:
    def __init__(self, branch, belted_bias, opt_pressure):
        self.branch = branch
        self.belted_bias = belted_bias
        self.opt_pressure = opt_pressure
    
    def __str__(self):
        return ("Tyres: \n \tBranch: " + self.branch +
               "\n \tBelted-bias: " + str(self.belted_bias) + 
               "\n \tOptimal pressure: " + str(self.opt_pressure))
    
class Engine:
    def __init__(self, fuel_type, noise_level):
        self.fuel_type = fuel_type
        self.noise_level = noise_level
    
    def __str__(self):
        return ("Engine: \n \tFuel type: " + self.fuel_type +
                "\n \tNoise level:" + str(self.noise_level))

class Body:
    def __init__(self,size):
        self.size = size
        
    def __str__(self):
        return "Body: \n \tsize: "+ self.size

class Car:
    def __init__(self, tyres, engine, body):
        self.tyres = tyres
        self.engine = engine
        self.body = body
    
    def __str__(self):
        return str(self.tyres)+ "\n" + str(self.engine) + "\n" + str(self.body)

t = Tyres('Pirelli', True, 2.0)
e = Engine('Diesel', 3)
b = Body('Medium')
c = Car(t, e, b)
print(c)
        



