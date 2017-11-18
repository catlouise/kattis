d = {
	'A': 11,
	'K': 4,
	'Q': 3,
	'J': 20,
	'T': 10,
	'9': 14,
	'8': 0,
	'7': 0
}

c = {
	'A': 11,
	'K': 4,
	'Q': 3,
	'J': 2,
	'T': 10,
	'9': 0,
	'8': 0,
	'7': 0
}

n, b = raw_input().split()
i = 0
score = 0
while i < 4*int(n):
	card = raw_input()
	if card[1] == b:
		score += d[card[0]]
	else:
		score += c[card[0]]
	i += 1
print score	
