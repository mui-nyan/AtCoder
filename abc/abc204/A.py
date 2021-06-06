import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]

def main():
    x,y = INTS()

    if x==y:
        print(x)
    else:
        if 0 not in (x,y):
            print(0)
        if 1 not in (x,y):
            print(1)
        if 2 not in (x,y):
            print(2)

main()
