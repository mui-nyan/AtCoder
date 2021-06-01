import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def GET(*types):
    strs = input().split()
    return [ t(s) for s,t in zip(strs, types)]
def get_nums_l():  return [ int(s) for s in input().split(" ")]
def get_all_int(): return map(int, open(0).read().split())
def log(*args): print("DEBUG:", *args, file=sys.stderr)

def main():

    n, p, q = INTS()
    A = INTS()

    ans = 0

    for a in range(n-4):
        x1 = A[a]
        for b in range(a+1, n-3):
            x2 = (x1 * A[b])%p
            for c in range(b+1, n-2):
                x3 = (x2 * A[c])%p
                for d in range(c+1, n-1):
                    x4 = (x3 *A[d])%p
                    for e in range(d+1, n):
                        if (x4*A[e])%p == q:
                            ans +=1
    
    print(ans)

main()
