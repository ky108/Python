coffee = 0
tasks = ('coding', 'dog', 'cat', 'movie')
while True:
    line = input()
    if line == 'END':
        break

    if line == 'coding' or line == 'dog' or line == 'cat' or line == 'movie':
        coffee += 1
        # if line.isupper():
    elif line == 'CODING' or line == 'DOG' or line == 'CAT' or line == 'MOVIE':
        coffee += 2
    else:
        continue

if coffee > 5:
    print('You need extra sleep')
else:
    print(coffee)