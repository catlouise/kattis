import sys
name = sys.stdin.readline().strip().split('-')
autori = ''

for i in name:
    autori += i[0]
print(autori)
