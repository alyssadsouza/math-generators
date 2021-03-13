# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 11:47:15 2020

@author: alyss
"""

def fact(n):
    count = 0
    if n == 1:
        return 1
    else:
        count += n*fact(n-1)
    return count

print(fact(5))

