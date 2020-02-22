def moar(a, b, n):
    def count_mult(tup, n):
        cnt = 0
        for x in tup:
            if x % n == 0:
                cnt += 1
        return cnt
    
    return count_mult(a, n) > count_mult(b, n)

