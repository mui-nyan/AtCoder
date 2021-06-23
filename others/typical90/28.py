from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    
    imosu = [ [0] * (1001) for _ in range(1001) ]

    n = INT()
    for i in range(n):
        l,b,r,t = INTS()

        imosu[b][l] += 1
        imosu[b][r] -= 1
        imosu[t][l] -=1
        imosu[t][r] += 1

    for y in range(1001):
        for x in range(1, 1001):
            imosu[y][x] += imosu[y][x-1]
    for x in range(1001):
        for y in range(1, 1001):
            imosu[y][x] += imosu[y-1][x]

    count = defaultdict(int)
    for y in range(1001):
        for x in range(1001):
            count[imosu[y][x]] += 1
    for k in range(1, n+1):
        print(count[k])

main()
