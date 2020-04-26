import math
from functools import reduce
from collections import deque,defaultdict
import sys
sys.setrecursionlimit(10**7)

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

s = input()
X = list(map(int, list(s)))
n = len(s)

ruiseki = [0] * (n+1)
for i in (range(n-1, -1, -1)):
    # i桁目以降を10進数表記した値のmod 2019
    ruiseki[i] = (X[i] * pow(10, (n-i-1), 2019) + ruiseki[i+1]) % 2019

# log(ruiseki)

ans = 0
count = defaultdict(int)

for x in ruiseki:
    # log(count[x])
    ans += count[x]
    count[x] += 1
# log(count)
print(ans)
