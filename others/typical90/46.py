from collections import defaultdict, Counter
import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    MOD = 46

    n = INT()
    A = INTS()
    B = INTS()
    C = INTS()

    A = [ n%MOD for n in A ]
    B = [ n%MOD for n in B ]
    C = [ n%MOD for n in C ]

    Ac = Counter(A)
    Bc = Counter(B)

    # AB[i] = A[a] + B[b] ≡ i (mod 46) となるようなa,bの選び方の数
    AB = defaultdict(int)
    for i in range(MOD):
        for j in range(MOD):
            AB[(i+j)%MOD] += Ac[i] * Bc[j]
    
    Cc = Counter(C)
    ans = 0
    for i in range(MOD):
        ans += AB[i] * Cc[(MOD-i)%MOD]
    
    print(ans)

main()
