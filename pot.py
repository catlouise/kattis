n = input()
total = 0 
i = 0 
while i < n:
    l = raw_input()
    ll = []
    for c in l:
        ll.append(c)
    x = "".join(ll[0:-1])
    p = ll[-1]
    total += int(x) ** int(p)
    i += 1
print total 
