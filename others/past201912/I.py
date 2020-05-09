import math
from functools import reduce
from collections import deque
from itertools import combinations
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def rangeI(it, l, r):
    for i, e in enumerate(it):
        if l <= i < r:
            yield e
        elif l >= r:
            break

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def subsets(items):
    _subsets_=[]
    for i in range(len(items) + 1):
        for c in combinations(items, i):
            _subsets_.append(c)
    return _subsets_


INF = 999999999999999999999999
MOD = 10**9+7

n,m = get_nums_l()

# ある部品の組み合わせを1回で買える最小コストのリスト
costs = [INF] * (2 ** (n+2))

for _ in range(m):
    s = input().split()
    items, cost = s[0], int(s[1])
    item_list = []
    for i, c in enumerate(items):
        if c == "Y":
            item_list.append(i)

    for s in subsets(item_list):
        keyn = 0
        for c in s:
            keyn += 2 ** c
        
        #print("keyn", keyn)
        if costs[keyn] > cost:
            costs[keyn] = cost

# そもそも買えない部品があったら無理
for i in range(0,n):
    if costs[2**i] == INF:
        print(-1)
        exit()

memo=[None] * (2 ** (n+2))

def solve(targets):

    lent = len(targets)
    
    # print(targets)

    if lent == 0:
        return 0

    if lent == 1:
        memo[2*list(targets)[0]] = costs[2*list(targets)[0]]
        # print(targets, costs[2**list(targets)[0]])
        return costs[2**list(targets)[0]]

    # all_s = set(targets)

    keyn=0
    for c in targets:
        keyn += 2 ** c
    
    if memo[keyn]:
        return memo[keyn]

    _min = costs[keyn]

    for s in subsets(targets):
        if len(s) in (0, lent):
            continue
        rev = targets.difference(s)
        cost = solve(s) + solve(rev)
        if _min > cost:
            _min = cost
    memo[keyn] = _min
    # print(targets, memo[keyn])
    return _min

ans = solve(set(range(0, n)))
# print(memo)
print(ans if ans < INF else -1)
