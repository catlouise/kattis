a, b = raw_input().strip().split()
if int(a[::-1]) > int(b[::-1]):
	print a.strip()[::-1]
else:
	print b.strip()[::-1]
