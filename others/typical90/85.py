import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def factorize(n, need_sort=True, reverse=False):
    """
    nの約数を列挙します。
    """
    a = [1]
    if n != 1:
        a.append(n)
    f = 2
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            if f != n//f:
                a.append(n//f)
        f += 1

    if need_sort:
        a.sort(reverse=reverse)

    return a

def main():
    k = INT()

    factors = factorize(k)
    # log(factors)
    m = len(factors)

    ans = 0
    for a in range(m):
        x = factors[a]
        for b in range(a, m):
            y = factors[b]
            if k % (x*y) == 0 and k // (x*y) >= y:
                ans += 1

    print(ans)

main()
