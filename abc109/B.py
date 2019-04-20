n = int(input())
words = []

prev_last=None
for i in range(n):
    w = input()
    if prev_last != None:
        if prev_last != w[0] or w in words:
            print("No")
            exit()
    prev_last = w[-1]
    words.append(w)

print("Yes")