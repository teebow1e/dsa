a,b = [int(val) for val in input().split()]

def pow(a,n):
    r = 1
    while n != 0:
        if n % 2 == 1:
            r = r * a
        a = a * a
        n = n // 2
    return r

print(pow(a,b))