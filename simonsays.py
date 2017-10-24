import sys
lines = int(sys.stdin.readline())
i = 0
while i < lines:
    line = sys.stdin.readline().split()
    if line[0] == 'Simon' and line[1] == 'says':
        print(' '.join(line[2:]))
    i += 1
