from collections import deque

m, n = eval(input())

matrix = [[0  for i in range(m)] for j in range(n)]
deq = deque([i for i in range(0, 10)])
up, bottom, left, right = 0, n, 0, m
i, j = 0, 0


while(left < right and up <= bottom):
    for j in range(left, right):
        matrix[up][j] = deq[0]
        deq.rotate(-1)
    up += 1

    if up == bottom:
        break

    for i in range(up, bottom):
        matrix[i][right - 1] =  deq[0]
        deq.rotate(-1)
    right -= 1

    if left == right:
        break
    for j in range(right - 1, left - 1, -1):
        matrix[bottom - 1][j] = deq[0]        
        deq.rotate(-1)
    bottom -= 1
 
    if up == bottom:
        break
    for i in range(bottom - 1, up - 1, -1):
        matrix[i][left] = deq[0]
        deq.rotate(-1)
    left += 1

for i in range(0, n):
    for j in range (0, m):
        end = ' ' if j != m - 1 else '\n'
        print(matrix[i][j], end=end)