import sys
amount = int(sys.stdin.readline())
temps = sys.stdin.readline().split()
below = 0

for t in temps:
    if int(t) < 0:
        below += 1

print(below)
