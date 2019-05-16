k = int(input())
nums = reversed([ int(s) for s in input().split(" ")])

pass_min = 2
pass_max = 2
for n in nums:

    # pass_min = このラウンドを通過する人数の下限
    # pass_max = このラウンドを通過する人数の上限

    # pass_min以上の最小のnの倍数
    aaa = pass_min + (n - pass_min % n) % n

    # pass_max以下の最大のnの倍数
    bbb = pass_max - pass_max % n

    # 不可能チェック
    if aaa > pass_max or bbb < pass_min:
        print(-1)
        exit()
    
    pass_min = aaa
    pass_max = bbb + (n - 1)

print(pass_min, pass_max)