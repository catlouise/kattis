n = input()
i = 0
while i < n:
	line = raw_input()
	alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
	for c in line:
		if c.lower() in alpha:
			alpha.remove(c.lower())
	if len(alpha) > 0:
		print 'missing {}'.format(''.join(alpha))
	else:
		print 'pangram'
	i += 1
