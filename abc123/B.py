

arr=[int(input()),int(input()),int(input()),int(input()),int(input())]
min=99
min_index=-1
for i,t in enumerate(arr):
    t_mod10 = t % 10
    if t_mod10 != 0 and t_mod10 < min:
        min = t_mod10
        min_index = i

sum = 0
for i,t in enumerate(arr):
    if i == min_index:
        sum += t
    else:
        sum += (t + 9) // 10 * 10

print(sum)