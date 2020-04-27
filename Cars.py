#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:10:53 2020

@author: ctralie
"""

class KatsClass(object):
    def set_name(self, name):
        self.name = name

kat = KatsClass()
kat.name = "Kat"


class Car(object):
    count = 0
    
    def __init__(self, make, model, year):
        """
        Constructor.  Saves away properties
        """
        self.make = make
        self.model = model
        self.year = year
        self.x = 0
        self.y = 0
        Car.count = Car.count + 1
    
    def move_to_right(self):
        self.x = self.x + 1
    
    def __str__(self):
        """
        Return a string which is a representative
        of this particular object
        """
        return "%i"%self.year + " " + self.make + " " + self.model


class ColorCar(Car):
    def __init__(self, make, model, year, color):
        Car.__init__(self, make, model, year)
        self.color = color
    
    def move_to_right(self):
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
print(chris.x)


celia = Car("honda", "crv", 2009)
celia.move_to_right()
print(celia)

brock = Car("porsche", "718 Cayman S.", 2017)

print("There are", Car.count, "cars now")
