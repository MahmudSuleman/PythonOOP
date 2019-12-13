# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:48:11 2019

@author: Chamtooni
"""

class Person:
    def __init__(self, fname, lname, email):
        self.firstName = fname
        self.lastName = lname
        self.email = email
        
    def fullName(self):
         return "{} {}".format(self.firstName, self.lastName)
     
person_1 = Person("Mudi","Sheikh", "mudisheikh@outlook.com")

print(person_1.fullName())
        
        
     
        
        
        
        
     
        

