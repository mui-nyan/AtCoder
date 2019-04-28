import math

q = int(input())

for i in range(q):
    a,b,c,d = map(int, input().split(" "))

    char_1 = "A"
    char_2 = "B"

    if b > a:
        char_1 = "B"
        char_2 = "A"

    max_aaa = math.ceil(max(a,b) / (min(a,b)+1))
    len_pattern = max_aaa + 1

    if b > a:
        pattern = "A" + "B" * max_aaa
    else:
        pattern = "A" *max_aaa + "B"

    len_ans = d - c + 1
    ans = ""
    

    
    for i in range(c-1, d):
        if i != len_ans - 1:
            ans += pattern[i % len_pattern]
        else:
            # Aを使い切っている場合はBにする
            if (i // len_pattern * max_aaa + i % len_pattern) == max(a,b):
                ans += char_2
            else:
                ans += char_1
    
    print(ans)