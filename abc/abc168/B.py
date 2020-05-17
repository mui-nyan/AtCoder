import sys

def input():
    return sys.stdin.readline().strip()

k = int(input())
s = input()

if len(s) <= k:
    print(s)
else:
    print(s[:k] + "...")
