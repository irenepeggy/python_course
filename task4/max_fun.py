def maxfun(s, f1, *fmas):
    maxf = f1
    max_sum = sum([f1(x) for x in s])
    for f in fmas:
        new_sum = sum([f(x) for x in s])
        if new_sum >= max_sum:
            maxf = f
            max_sum = new_sum
    return maxf

