allowance = input()
months = input() 
total = allowance 
i = 0
while i < months:
    used = input()
    total += allowance - used
    i += 1 
print total 
