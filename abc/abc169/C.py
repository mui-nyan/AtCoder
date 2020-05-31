import sys
from decimal import Decimal

def input():
    return sys.stdin.readline().strip()

S = input().split()
a = Decimal(S[0])
b = Decimal(S[1])

print(int(a*b))
