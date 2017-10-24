t = 0
c = 0
g = 0 
s = raw_input().strip()
for i in s:
    if i == 'T':
        t += 1
    elif i == 'C':
        c += 1
    elif i == 'G':
        g += 1
score = 0 
j = 0 
while t > j and c > j and g > j:
    score += 7 
    j += 1

print score + t ** 2 + c ** 2 + g ** 2
