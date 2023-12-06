a,b = [int(val) for val in input().split()]

MOD_VAL = 10**9 + 7

def pow_mod(a,n):
    a = a % MOD_VAL
    res = 1
    while n != 0:
        if n % 2 == 1:
            res = (res * a) % MOD_VAL
        a = (a * a) % MOD_VAL
        n = n // 2
    return res

print(pow_mod(a,b))