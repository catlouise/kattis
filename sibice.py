from math import sqrt 
box = raw_input().strip().split()
n = int(box[0])
longest = sqrt(int(box[1])**2+int(box[2])**2)
i = 0
while i < n:
    m = input()
    if m <= longest:
        print 'DA'
    else:
        print 'NE'
    i += 1
