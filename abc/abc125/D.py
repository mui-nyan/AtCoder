n = int(input())
nums = [int(s) for s in input().split(" ")]

absmin=abs(nums[0])
abssum=0
minus=0

for n in nums:
    if n < 0:
        minus += 1
    absmin = min(absmin, abs(n))
    abssum += abs(n)

if minus % 2 == 0:
    print(abssum)
else:
    print(abssum - (absmin * 2))
