n, bats = input(), raw_input().strip().split()
i, total = 0, 0
for bat in bats:
	if bat != '-1':
		i += 1.0
		total += float(bat)
print total/i
