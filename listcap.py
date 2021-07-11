# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 17:14:07 2021

@author: Ashwin
"""

list1=[1,2,2.3,4.5,"Ashwin","Vishal","a",2,1]
list2=[5,6,7]
list1.append("suriya")
print(list1)
x=list1.count(2)
print(x)
y=list1.copy()
print(y)
list1.extend(list2)
print(list1)
z=list1.index("Ashwin")
print(z)
list1.pop(5)
print(list1)
list1.remove("Ashwin")
print(list1)
list1.reverse()
print(list1)
list2.sort(reverse=True)
print(list2)
list1.clear()
print(list1)