import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n = INT()
    # 最後に番兵
    s = input() + "!"

    # すべての選び方の数
    total = n * (n+1) // 2

    # oとxが両方 "含まれない" 区間をしゃくとり法で探索し、全体から引く
    complement = 0
    tail = 0
    head = 0

    while head < n:
        while s[head] == s[tail]:
            head += 1
        while tail < head:
            complement += head-tail
            tail += 1

    print(total - complement)

main()
