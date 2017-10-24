n = input()
while n != -1:
    i = 0
    total_time = 0
    dist = 0
    while i < n:
        mt = raw_input().strip().split()
        speed = int(mt[0])
        time = int(mt[1]) - total_time 
        total_time = int(mt[1])
        dist += time * speed
        i += 1 
    print str(dist) + ' miles'
    n = input()
