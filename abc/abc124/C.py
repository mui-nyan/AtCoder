s=input()

now_black=True
count_a=0
for c in s:
    if now_black and c == "1":
        count_a += 1
    elif (not now_black) and c == "0":
        count_a += 1
    now_black = not now_black

now_black=False
count_b=0
for c in s:
    if now_black and c == "1":
        count_b += 1
    elif (not now_black) and c == "0":
        count_b += 1
    now_black = not now_black

print (min(count_a, count_b))