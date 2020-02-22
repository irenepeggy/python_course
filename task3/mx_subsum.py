
val = eval(input())
cur_subsum = val
total_max_subsum = val


while (val != 0):
    val = eval(input())
    if (val == 0):
        break
    cur_subsum = max(val, val + cur_subsum)
    total_max_subsum = max(cur_subsum, total_max_subsum)

print(total_max_subsum)