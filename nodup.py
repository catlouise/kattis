line = raw_input().strip().split()
words = []
dup = 'yes'
for l in line:
	if l in words:
		dup = 'no'
		break
	else:
		words.append(l)	
print dup	
