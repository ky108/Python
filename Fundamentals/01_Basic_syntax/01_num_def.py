n = float(input())
if n == 0:
    print('zero')
else:
    if abs(n) < 1:
        print(f'small', end=' ')
    elif abs(n) > 1000000:
        print(f'large', end=' ')

    if n > 0:
        print('positive')
    else:
        print('negative')

 
# n = float(input())
#
# if n == 0:
#     print('zero')
# elif n > 0:
#     if n <1:
#         print('small positive')
#     elif n > 1000000:
#         print('large positive')
#     else:
#         print('positive')
# else:
#     if abs(n) < 1:
#         print('small negative')
#     elif abs(n) > 1000000:
#         print('large negative')
#     else:
#         print('negative')
