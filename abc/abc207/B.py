import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    a,b,c,d = INTS()
    x = a
    y = 0
    for i in range(10**6):
        if x <= y*d:
            print(i)
            return
        x += b
        y += c
    print(-1)

main()
