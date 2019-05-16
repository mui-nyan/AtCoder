
ans = 4 ** 5

for a in ["a", "g", "c", "t"]:
    for b in ["a", "g", "c", "t"]:
        for c in ["a", "g", "c", "t"]:
            for d in ["a", "g", "c", "t"]:
                for e in ["a", "g", "c", "t"]:
                    s = a+b+c+d+e
                    if "agc" in s or "acg" in s or "gac" in s \
                        or "atgc" in s or "agtc" in s or "aggc" in s:
                        ans -= 1
                        print(s)

print (ans)
    