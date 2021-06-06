import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]

def main():
    n = INT()
    A = INTS()

    ans = 0

    for a in A:
        if a > 10:
            ans += a-10

    print(ans)

main()
