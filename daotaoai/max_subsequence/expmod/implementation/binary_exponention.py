a,b = [int(val) for val in input().split()]

def pow(a,n):
    res = 1
    while n != 0:
        if n % 2 == 1:
            res = res * a
        a = a * a
        n = n // 2
    return res

print(pow(a,b))