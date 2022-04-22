import math

num = int(input("Enter the number of rows:"))

for n in range(0, num + 1):
    print(' ', end='\n')
    for r in range(0, n + 1):
        c = math.comb(n, r)
        print('', c, sep=' ', end='')







