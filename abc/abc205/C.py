import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    a,b,c = INTS()

    if c % 2 == 0:
        a = abs(a)
        b = abs(b)

    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")

main()
