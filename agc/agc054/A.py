import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main(n,s):
    first = s[0]
    last = s[-1]

    if first != last:
        print(1)
        return
    
    for i in range(1, n-1):
        if s[i] != first and s[i+1] != last:
            print(2)
            return
    
    print(-1)

n = INT()
s = input()

main(n,s)
