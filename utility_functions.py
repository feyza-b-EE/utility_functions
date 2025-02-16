# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 18:38:12 2023

@author: Feyza
"""
my_name = "Ayse Feyza Birer"
my_id = "220102002033"
my_email = "a.birer2022@gtu.edu.tr"


def problem1(s):
    
    def find_the_king(s):
        for i in s:
            if i == "K":
                return True 
        return False
    
    return find_the_king(s)

        
def problem2(a,b,c,d):
    x = [a,b,c,d]
    y = float(min(x))
    return y 

def problem3(a,b):
    if a > b:
        if a < 0 and b < 0:
            return int(a) - 1
        elif round(a) == round(b)+1 :
            if round(a)-b == 0.5:
                return round(a)
            else:
                return int(a)
        elif round(a) == round(b):
            return round(a)
        else:
            return int(a)

    if a < b:
        if round(a) == int(a) and round(a) != a :
            return round(a) + 1
        elif round(a) == int(a) + 1:
            return int(a) + 1
        elif round(a) == a:
            return a 
        elif round(a) == int(a) - 1 :
            return int(a)

def problem4(radius=" ",height=" ", pi= 3.1415):
    
    volume = pi*radius*radius*height
    return volume
    
def problem5(radius=" ", height=" ", pi= 3.1415):
    
    radius_s = str(radius)
    height_s = str(height)
    pi_s = str(pi)    
    a ='0123456789.'
    
    for i in radius_s:
        if i not in a :
            return -1
    for i in height_s:
        if i not in a:
            return -1
    for i in pi_s:
        if i not in a:
            return -1   
   
    volume = pi * radius * radius * height

    return volume

def problem6(a):
    myDict = {}
    
    for i in a:
        if i in myDict:
            myDict[i] += 1
        else:
            myDict[i] = 1 
            
    for i in myDict:
        if myDict[i] == 1:
            return i
            
def problem7(a):
    b = list(a)
    if b == sorted(list(a)):
        return True
    else:
        return False
    
def problem8(a):
    myDict = {}
    for i in a:
        if i in myDict:
            myDict[i] += 1
        else:
            myDict[i] = 1
        
    for i in myDict:
        if myDict[i] > 1:
            return False
    return True
    
    
    
    
    
    
    
    
    
    
    
    
    
