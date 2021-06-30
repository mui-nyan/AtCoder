import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def GET(*types):
    strs = input().split()
    return [ t(s) for s,t in zip(strs, types)]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def to_nine(n):
    if n == 0:
        return "0"
    
    s = ""
    while n>0:
        s += str(n%9)
        n //= 9
    return s[::-1]

def to_oct(n):
    if n == 0:
        return "0"
    
    s = ""
    while n>0:
        s += str(n%8)
        n //= 8
    return s[::-1]

def main():

    s, k = GET(str, int)

    for _ in range(k):
        n = int(s, base=8)
        s = to_nine(n)
        s = s.replace("8", "5")

    print(s)

main()
