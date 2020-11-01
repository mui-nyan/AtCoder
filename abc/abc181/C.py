import sys

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

def main():
    INF = 999999999999999999999999
    MOD = 10**9+7

    n = int(input())

    P = []

    for i in range(n):
        x,y = get_nums_l()
        P.append((x,y))
    
    for i in range(n-2):
        a = P[i]
        for j in range(i+1, n-1):
            b = P[j]
            for k in range(j+1, n):
                c = P[k]
                x1 = a[0] - b[0]
                y1 = a[1] - b[1]
                x2 = a[0] - c[0]
                y2 = a[1] - c[1]

                if y1*x2 == y2*x1:
                    print("Yes")
                    exit()
    
    print("No")

main()
