#!/usr/bin/env python3

def print_fibonacci(length):    
    if length <= 0:
        print([])
    elif length == 1:
        print([0])
    elif length > 1:
        counter = length
        sequence = [0,1]
        while len(sequence) < counter:
            last = sequence[-1]
            second_last = sequence[-2]
            next = (second_last + last)
            sequence.append(next)
        print(sequence)