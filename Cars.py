#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:10:53 2020

@author: ctralie
"""




class Car(object):
    count = 0 # This is a global variable of the clas
    # which isn't tied to a particular object
    
    def __init__(self, make, model, year):
        """
        Constructor.  Saves away properties
        """
        self.make = make
        self.model = model
        self.year = year
        self.x = 0
        self.y = 0
        # Increment the global variable
        Car.count = Car.count + 1
    
    def move_to_right(self):
        self.x = self.x + 1
    
    def move_up(self):
        self.y = self.y + 1
    
    def __str__(self):
        """
        Return a string which is a representative
        of this particular object
        """
        return "%i"%self.year + " " + self.make + " " + self.model


"""
This is a more specific Car class which "inherits" the 
behavior from Car.  We can redefine the behavior of specific
methods to change what they do for a color car.  Otherwise,
they will rever to what they did in Car
"""
class ColorCar(Car):
    def __init__(self, make, model, year, color):
        # First call the constructor on the parent car class
        Car.__init__(self, make, model, year)
        # Now we can do other stuff
        self.color = color
    
    def move_to_right(self):
        # We could decide that a color car moves 
        # by 2 units to the right each time, but
        # since we don't redefine move_up, it will
        # do by default what move_up did in car
        self.x = self.x + 2
    
    def __str__(self):
        """
        Return a string which is a representative
        of this particular object
        """
        return "%i"%self.year + " " + self.make + " " + self.model + " " + self.color


chris = ColorCar(color="silver", make="honda", year=2010, model="civic")
for i in range(20):
    chris.move_to_right()
print(chris)
print(chris.x)


celia = Car("honda", "crv", 2009)
celia.move_to_right()
print(celia)

brock = Car("porsche", "718 Cayman S.", 2017)

print("There are", Car.count, "cars now")




"""
KatsClass is demonstrating what happens
if we don't have a constructor __init__.
We still need to say KatsClass() to make an
object, but nothing else happens at that point.
We have to "override" the default behavior by
defining __init__ if we want to do something different
"""
class KatsClass(object):
    def set_name(self, name):
        self.name = name

kat = KatsClass()
kat.name = "Kat"