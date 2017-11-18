cost = input()
lawns = input()
i, total = 0, 0 
while i < lawns:
	size = raw_input().split()
	total += float(size[0]) * float(size[1]) * cost
	i += 1
print total
