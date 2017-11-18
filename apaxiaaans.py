name = raw_input()
compact = []
last = ''
for l in name:
	if l != last:
		compact.append(l)
		last = l
print ''.join(compact)
