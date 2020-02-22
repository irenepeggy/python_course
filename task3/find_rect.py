
bound_row = input()

rows = []

row = input()

while (row != bound_row):
    rows.append(row)
    row = input()


m = len(row)
n = len(rows)

count = 0
for i in range(0, n):
    for j in range(0, m):
        if (rows[i][j] == '#'):
            if ((i == 0 or rows[i - 1][j] == '.') and (j == 0 or rows[i][j - 1] == '.')):
                count += 1
print(count)