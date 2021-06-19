from collections import Counter
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n = INT()
    A = INTS()

    counter = Counter(A)
    all = n*(n-1)//2
    match = 0
    for v,c in counter.items():
        if c >= 2:
            match += c * (c-1) // 2
    
    print(all-match)

main()
