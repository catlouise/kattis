tests = input()
i = 0 
while i < tests:
	lines, cols = raw_input().strip().split()
	j = 0 
	mirror = []
	print 'Test {}'.format(i+1)
	while j < int(lines):
		mirror.append(raw_input()[::-1])
		j += 1
	for m in mirror[::-1]:
		print m
	i += 1
