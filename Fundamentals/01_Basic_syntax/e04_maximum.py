divisor = int(input())
max_num = int(input())
for num in range(max_num, 0, -1):
    if num % divisor == 0:
        print(num)
        break


# max_final = 0
# for num in range(1, max_num + 1):
#     if num % divisor == 0:
#         max_final = num
# print(max_final)


# for num in range(1, max_num + 1):
#     if num % divisor == 0:
#         if num >= max_final:
#             max_final = num
