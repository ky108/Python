while True:
    name = input()
    if name == 'Welcome!':
        break
    if name == 'Voldemort':
        print('You must not speak of that name!')
        exit()

    elif len(name) < 5:
        print(f'{name} goes to Gryffindor.')
    elif len(name) == 5:
        print(f'{name} goes to Slytherin.')
    elif len(name) == 6:
        print(f'{name} goes to Ravenclaw.')
    elif len(name) > 6:
        print(f'{name} goes to Hufflepuff.')

print('Welcome to Hogwarts.')

# Luna
# Hermione
# Neville
# Voldemort
