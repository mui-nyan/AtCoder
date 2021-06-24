from functools import reduce
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def mex(nums):
    """numsに含まれない最小の非負整数を返します。"""
    for i in range(10000):
        if i not in nums:
            return i
    return None

def main():
    n = INT()
    W = INTS()
    B = INTS()

    # grundy[w][b] = 1つの山について、白石がw個,青石がb個ある場合のgrundy数
    grundy = [ [0] * (2000) for _ in range(51) ]
    grundy[0][1] = 0

    for w in range(51):
        for b in range(1500):
            # nums = この状態から遷移できる局面のgrundy数の集合
            nums = set()
            if w >= 1:
                nums.add(grundy[w-1][b+w])
            if b >= 2:
                for i in range(1, b//2+1):
                    nums.add(grundy[w][b-i])
            grundy[w][b] = mex(nums)
    
    grundys = [ grundy[w][b] for w,b in zip(W,B) ]
    x = reduce(lambda a,b:a^b, grundys)

    print("First" if x != 0 else "Second")

main()
