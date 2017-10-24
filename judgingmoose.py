t = raw_input().strip().split()
l = int(t[0])
r = int(t[1])

if r == 0 and l == 0:
    print "Not a moose"
elif l == r:
    print "Even " + str(l+r)
elif l > r:
    print "Odd " + str(2*l)
else:
    print "Odd " + str(2*r)
