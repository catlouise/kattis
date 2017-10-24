n = input()
i = 0 
while i < n:
    r = raw_input().strip().split()
    if int(r[0]) == int(r[1]) - int(r[2]):
        print 'does not matter' 
    elif int(r[0]) < int(r[1]) - int(r[2]):
        print 'advertise'
    else:
        print 'do not advertise'
    i += 1 
