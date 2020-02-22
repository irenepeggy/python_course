from math import *

def compute(x, func):
    eval(func)

func = input()
sect = eval(input())
a,b = sect
x = a
if (eval(func) > 0):
    a, b = sect[1], sect[0]

eps = 0.000001
x = (a + b) / 2
f_value = eval(func)

while(abs(f_value) > eps):


    if (f_value > 0):
        b = x
    else:
        a = x
    x = (a + b) / 2

    f_value = eval(func)

print(x)
