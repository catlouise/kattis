n, i = input(), 0
while i < n:
	a, b = raw_input(), raw_input()
	dif, j = [], 0
	while j < len(a):
		if a[j] == b[j]:
			dif.append('.')
		else:
			dif.append('*')
		j += 1
	print a
	print b
	print ''.join(dif)
	print ''
	i += 1
