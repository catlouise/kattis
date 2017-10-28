import sys
n = int(sys.stdin.readline())
i = 0
while i < n:
	line = sys.stdin.readline().strip().split()
	if ' '.join(line[0:2]) == "simon says" :
		print ' '.join(line[2:])
	else:
		print ' '
	i += 1
