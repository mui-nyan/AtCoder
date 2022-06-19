import math
import sys

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]

def min_multiple_of_k(a, k):
    """a以上で最小のkの倍数を求めます。"""
    return a + (k-a%k)%k

def max_multiple_of_k(a, k):
    """a以下で最大のkの倍数を求めます。"""
    return a - a%k

def div_ceil(a, b):
    """a÷bの切り上げを求めます。"""
    return (a + b - 1) // b

def sum_to(a, b, k=1):
    """a以上b以下のkの倍数の合計を求めます。"""
    a = min_multiple_of_k(a, k)
    b = max_multiple_of_k(b, k)
    n = b - a + 1
    return (a + b) * div_ceil(n, k) // 2

def lcm(m, n):
    return m*n//math.gcd(m,n)

def main():
    n, a, b = INTS()
    print(sum_to(1, n) - sum_to(1, n, a) - sum_to(1, n, b) + sum_to(1, n, lcm(a, b)))

main()
