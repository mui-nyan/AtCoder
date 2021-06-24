import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    h,w = INTS()

    if min(h,w) == 1:
        print(max(h,w))
        return

    print(((h+1)//2) * ((w+1)//2))

main()
