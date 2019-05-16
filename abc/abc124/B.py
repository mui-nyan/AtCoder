n=int(input())
h_arr=[int(s) for s in input().split(" ")]

hmax=0
count = 0
for h in h_arr:
    if h >= hmax:
        count += 1
        hmax = h
print (count)