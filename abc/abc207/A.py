import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    a,b,c = INTS()
    print(sum((a,b,c)) - min((a,b,c)))

main()
