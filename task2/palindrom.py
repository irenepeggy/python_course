num = eval(input())

temp = num
reversed_num = 0

while temp > 0:
    reversed_num = reversed_num * 10 + temp % 10
    temp //= 10

print('YES' if reversed_num == num else 'NO')