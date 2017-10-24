s = raw_input()
b = 1
for c in s:
    if c == 'A' and (b == 1 or b == 2):
        if b == 1:
            b = 2
        else:
            b = 1
    elif c == 'B' and (b == 2 or b == 3):
        if b == 2:
            b = 3
        else:
            b = 2
    elif c == 'C' and (b == 1 or b == 3):
        if b == 3:
            b = 1
        else:
            b = 3
print b
