word = raw_input()
last = ''
hiss = 'no hiss'
for c in word:
	if c == 's' and last == 's':
		hiss = 'hiss'
		break
	last = c
print hiss
