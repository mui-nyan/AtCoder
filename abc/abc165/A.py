import sys
sys.setrecursionlimit(10**7)

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

MOD = 10**9+7

k= int(input())
a,b = get_nums_l()

print("OK" if a%k==0 or b-a+1 > k or a%k>b%k else "NG") 