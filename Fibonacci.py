# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:08:16 2020

@author: Alyssa
"""


def fibonacci_up_to(n):
    
    '''
    returns fibonacci sequence up to n
    assumes n >= 0
    '''
    sequence = []
    sequence_string = ''
    (a, b) = (0, 1)
    
    while a <= n:
        sequence.append(a)
        (a, b) = (b, a + b)
    
    for num in sequence:
        if num == sequence[-1]:
            sequence_string += str(num)
        else:
            sequence_string += str(num) + ' '
    
    return sequence_string
        

def fibonacci_length_of(n):
    
    '''
    returns fibonacci sequence of n terms
    '''
    count = 0
    sequence = []
    sequence_string = ''
    (a, b) = (0, 1)
    
    while count < n:
        sequence.append(a)
        (a, b) = (b, a + b)
        count += 1
    
    for num in sequence:
        if num == sequence[-1]:
            sequence_string += str(num)
        else:
            sequence_string += str(num) + ' '

    
    
    return sequence_string


def fib_recur(x):
    
    '''
    assumes x is an int >= 0
    returns fibonnaci of x
    '''
    
    if x == 0 or x == 1:
        return 1
    else:
        return fib_recur(x-1) + fib_recur(x-2)

print(fibonacci_length_of(10))