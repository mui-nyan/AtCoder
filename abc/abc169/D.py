import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())

if n == 1:
    print(0)
    exit()

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

    if len(arr) == 0:
        arr.append((n, 1))
    return arr

fac_ = prime_factorize(n)
fac = Counter(fac_)

ans = 0
for p,e in fac.items():
    x = e
    for i in range(1, 99999999):
        if x >= i:
            x -= i
            ans += 1
        else:
            break

print(ans)
