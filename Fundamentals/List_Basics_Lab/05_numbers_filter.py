# n = int(input())
# even = []
# odd = []
# negative = []
# positive = []
# for _ in range(n):
#     num = int(input())
#     if num >= 0:
#         positive.append(num)
#     else:
#         negative.append(num)
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)
#
# select = input()
# filtered = eval(select)
# print(filtered)

# if select == "even":
#     print(even)
# elif select == "odd":
#     print(odd)
# elif select == "positive":
#     print(positive)
# else:
#     print(negative)


n = int(input())
nums = []
for _ in range(n):
    number = int(input())
    nums.append(number)

select = input()
filtered = []
for num in nums:
    if select == "even" and num % 2 == 0:
        filtered.append(num)
    if select == "odd" and num % 2 != 0:
        filtered.append(num)
    if select == "positive" and num >= 0:
        filtered.append(num)
    if select == "negative" and num < 0:
        filtered.append(num)
print(filtered)

# 3
# 111
# -4
# 0
# negative
