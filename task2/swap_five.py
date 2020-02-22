from math import *
k = eval(input())

if (k == 1):
    x = 0
else:
    dec = 10
    denom = k * 10 - 1
    mod = (k * dec - k * k) % denom
    
    while (mod):
        dec *= 10
        mod = (k * dec - k * k) % denom

    x = (k * dec - k * k)// denom

print (x * 10 + k)