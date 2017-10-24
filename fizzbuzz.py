import sys
line = sys.stdin.readline().strip().split()
f = int(line[0])
b = int(line[1])
n = int(line[2])
i = 1

while i <= n:
    if i % f == 0 and i % b == 0:
        print('FizzBuzz')
    elif i % f == 0:
        print('Fizz')
    elif i % b == 0:
        print('Buzz')
    else:
        print(i)
    i+=1
