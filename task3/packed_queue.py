from collections import deque

seq = eval(input())
deq = deque([])

for elem in seq:
    if (type(elem) is tuple):
        deq.extend(elem)
    elif (len(deq) < elem):
        break
    else:
        print(tuple([deq.popleft() for i in range(elem)]))

