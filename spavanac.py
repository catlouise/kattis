time = raw_input().strip().split()
hour = int(time[0])
mins = int(time[1])

if mins >= 45:
    print str(hour) + ' ' + str(mins - 45)
else:
    if hour == 0:
        print '23' + ' ' + str(mins + 15)
    else:
        print str(hour - 1) + ' ' + str(mins + 15)
