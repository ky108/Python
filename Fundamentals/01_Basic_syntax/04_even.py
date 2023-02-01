n = int(input())

for _ in range(n):
    num = int(input())

    if num % 2 != 0:
        print(f'{num} is odd!')
        break
else:
    print("All numbers are even.")


# even = True
# for _ in range(n):
#     num = int(input())
#     if num % 2 != 0:
#         print(f"{num} is odd!")
#         even = False
#         break
# if even:
#     print("All numbers are even.")

