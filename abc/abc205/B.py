import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n = INT()
    A = INTS()

    for i in range(1, n+1):
        if i not in A:
            print("No")
            return
    print("Yes")

main()
