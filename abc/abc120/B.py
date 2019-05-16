tmp=input().split(" ")
a = int(tmp[0])
b = int(tmp[1])
k = int(tmp[2])

count=0
for n in range(max(a,b), 0, -1):
    if a % n == 0 and b % n == 0:
        count += 1
        if count == k:
            print(n)
            exit()
