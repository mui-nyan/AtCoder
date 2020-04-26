from collections import defaultdict
import sys

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

n,p = get_nums_l()
s = input()
X = list(map(int, list(s)))
n = len(s)

if p in (2,5):
    # 2,5の倍数は1桁目だけで判定できる。
    # 10と互いに素でないので、後半の判定法では判定できない。
    ans = 0
    for i,x in enumerate(X):
        if x%p == 0:
            ans += i+1
    print(ans)
else:
    ruiseki = [0] * (n+1)
    for i in (range(n-1, -1, -1)):
        # i桁目以降を10進数表記した値のmod p
        ruiseki[i] = (X[i] * pow(10, (n-i-1), p) + ruiseki[i+1]) % p

    # log(ruiseki)

    ans = 0
    count = defaultdict(int)

    for x in ruiseki:
        # log(count[x])
        ans += count[x]
        count[x] += 1
    # log(count)
    print(ans)
