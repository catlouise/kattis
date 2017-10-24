import sys
line = sys.stdin.readline().split()
art = float(line[0])
fac = float(line[1])
cit = 0.0

while cit/art < fac-1.0:
    cit+=1.0
print(int(cit)+1)
