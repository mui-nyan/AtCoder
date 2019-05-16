import re

str=input()

arr = re.split(r'[^AGCT]', str)

m=0
for part in arr:
    m = max(m, len(part))

print (m)