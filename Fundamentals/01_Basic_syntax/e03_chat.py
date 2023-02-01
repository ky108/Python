n = int(input())
for _ in range(n):
    code_num = int(input())
    if code_num == 88:
        print('Hello')
    elif code_num == 86:
        print('How are you?')
    elif code_num < 88:
        print('GREAT!')
    else:
        print('Bye.')
