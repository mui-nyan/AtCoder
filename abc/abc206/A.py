import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n = INT()
    x = int(n*1.08)

    if x < 206:
        print("Yay!")
    elif x == 206:
        print("so-so")
    else:
        print(":(")

main()
