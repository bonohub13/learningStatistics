#!/usr/bin/python3

def mean(data):
    return sum(data)/len(data)

def median(data):
    n = len(data)
    if n%2 == 0:
        median = (data[n//2-1]+data[n//2])/2
    else:
        median = (data[n//2+1])
    
    return median
