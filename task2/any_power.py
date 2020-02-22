from math import *

num = eval(input())
checked_root = 2
root = pow(num, 1/checked_root)

while (root >= 2):
    if isclose(root, ceil(root)) or isclose(root, trunc(root)):
        print('YES')
        break
    checked_root += 1
    root = pow(num, 1/checked_root)
else:
    print('NO')
