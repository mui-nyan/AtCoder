tmp=input().split(" ")
n = int(tmp[0])
k = int(tmp[1])

s=input()

def sumrange(arr, l, r):
    #print("sumrange:", l, r, arr[r] - arr[l-1])
    return arr[r] - arr[l-1]

prev="1"
counts=[0]
count=0
prev_count=0
for c in s:
    if c == prev:
        count+=1
    else:
        counts.append(prev_count + count)
        prev=c
        prev_count += count
        count=1
else:
    counts.append(prev_count + count)

#print(counts)

w = k * 2 + 1
#print(w)

max_score=0
for i in range(0, len(counts)-1, 2):
    if(i + 1 >= len(counts)):
        break
    l = i+1
    r = min(l + w - 1, len(counts)-1)
    score = sumrange(counts, l, r)
    max_score = max(max_score, score)

print(max_score)