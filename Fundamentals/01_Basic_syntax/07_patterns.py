n = int(input())

for x in range(1, n + 1):
    for y in range(x):
        print('*', end='')
    print()

for a in range(n - 1, -1, -1):
    for b in range(a):
        print('*', end='')
    print()
