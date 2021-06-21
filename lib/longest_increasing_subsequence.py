from bisect import bisect_left

def LIS(L):
    # dp1[i] = 長さ(i+1)の増加部分列の末尾として考えられる最小の値
    dp1 = []
    # dp2[i] = L[i]を末尾に置いた場合の最長増加部分列長
    dp2 = [0] * len(L)
    for i, ai in enumerate(L):
        pos = bisect_left(dp1, ai)
        dp2[i] = pos+1
        if len(dp1) <= pos:
            dp1.append(ai)
        else:
            dp1[pos] = ai
    return dp2
