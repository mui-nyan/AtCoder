from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def GET(*types):
    strs = input().split()
    return [ t(s) for s,t in zip(strs, types)]
def get_nums_l():  return [ int(s) for s in input().split(" ")]
def get_all_int(): return map(int, open(0).read().split())
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    h, w = INTS()
    grid = []
    for y in range(h):
        grid.append(INTS())

    ans = 0

    # 行の選び方を2**h通り全探索
    for bits in range(1, 2**h):
        G = []
        for y in range(h):
            if 2**y & bits != 0:
                G.append(grid[y])
        n = len(G)

        # この行の選び方で、数字が全て同じ列があれば、その数字の個数をカウントする
        count = defaultdict(int)

        for x in range(w):
            ok = True
            for y in range(n-1):
                if G[y][x] != G[y+1][x]:
                    ok = False
                    break
            if ok:
                count[G[0][x]] += 1
        
        for v,c in count.items():
            s = n * c
            if s > ans:
                ans = s

    print(ans)

main()
