import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n, l = INTS()
    k = INT()
    A = [0] + INTS() + [l]
    kaisa = [0] * (n+1)
    for i in range(n+1):
        kaisa[i] = A[i+1] - A[i]
    
    # log(kaisa)

    ok_max = 0
    ng_min = 10**9

    while ok_max + 1 < ng_min:
        mid = (ok_max + ng_min) // 2
        # ok = スコアをmid以上にできるか？

        ok = True

        now = 0
        cut = 0
        for a in kaisa:
            now += a

            if now >= mid:
                # ここで切る
                cut += 1
                now = 0
        
        ok = cut > k

        # log(mid, "OK" if ok else "NG")

        if ok:
            ok_max = mid
        else:
            ng_min = mid

    print(ok_max)

main()
