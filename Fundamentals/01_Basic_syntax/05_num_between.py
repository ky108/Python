# n = float(input())
# while 1 > n or n > 100:
#     n = float(input())
# print(f'The number {n} is between 1 and 100')

while True:
    n = float(input())
    # if n >= 1 and n <= 100:
    if 1 <= n <= 100:
        print(f'The number {n} is between 1 and 100')
        break


# 0.5
# 90
# -4
# 10

"""
n = 1
while n < 6:
    print(n)
    n += 1

for n in range(1, 6):
    print(n)
"""