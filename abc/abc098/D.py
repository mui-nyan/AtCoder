n = int(input())
nums = list(map(int, input().split(" ")))

ans = 0
tail = 0
prev = nums[0]

for head in range(1, n):
    num = nums[head]
    if prev & num > 0:
        # これ以上伸ばせない場合、
        # ここまでの長さ(head-tail)を正解に加算し、tailを進める
        while prev & num > 0:
            ans += head - tail
            # 区間値からtailを除外
            prev = prev ^ nums[tail]
            tail += 1
        prev += num
    else:
        # まだ伸ばせるなら区間値にheadを加えてそのまま進める
        prev = prev + num

count = n - tail
# 1からcountまでの合計を足す
ans += count*(count+1)//2

print(ans)