import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n,m = INTS()
    count = [0] * n
    for i in range(m):
        a,b = INTS()
        a-=1
        b-=1

        count[max(a,b)] += 1
    
    print(sum([ 1 if c==1 else 0 for c in count ]))

main()
