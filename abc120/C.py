s = input()

red=0
blue=0

for c in s:
    if c == "0":
        red += 1
    else:
        blue += 1

print(min(red, blue) * 2)