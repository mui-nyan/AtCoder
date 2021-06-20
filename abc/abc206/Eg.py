import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def GET(*types):
    strs = input().split()
    return [ t(s) for s,t in zip(strs, types)]
def get_nums_l():  return [ int(s) for s in input().split(" ")]
def get_all_int(): return map(int, open(0).read().split())
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def gcd(m, n):
    # 入力を m, n (m ≧ n) とする。
    tmp = max(m,n)
    n = min(m,n)
    m = tmp
    # n = 0 なら、 m を出力してアルゴリズムを終了する。
    if n == 0:
        return m
    # m を n で割った余りを新たに n とし、更に 元のnを新たにm とし 2. に戻る。
    return gcd(n, m % n)

def main():
    l,r = INTS()

    if l==1:
        l+=1
    if r==1:
        print(0)
        return

    ans = 0
    for x in range(l,r):
        for y in range(x+1,r+1):
            if gcd(x,y) > 1 and x%y!=0 and y%x!=0:
                ans += 2

    print(ans)

main()
