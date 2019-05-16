from functools import reduce


n = int(input())
nums = list(map(int, input().split(" ")))

ans = 0
prev = -1
count = 1 # 1が立ってるビットが一致しない数が連続している個数
left = -1

for i,num in enumerate(nums):
    if i == 0:
        prev = num
        left = 0
        count = 1
        continue
    
    #breakpoint()

    if prev & num > 0:
        # left を1進めたらいけるか？
        while prev & num > 0:
            ans += count
            prev = prev ^ nums[left]
            count -= 1
            left += 1
        count += 1
        prev += num
    else:
        count += 1
        prev = prev + num

#print("count", count)

# 1からcountまでの合計を足す
ans += count*(count+1)//2

print(ans)