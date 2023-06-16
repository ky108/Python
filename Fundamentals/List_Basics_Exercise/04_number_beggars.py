nums = input().split(", ")
count = int(input())
coins = [int(x) for x in nums]
outcome = [0] * count

index = 0
while index < len(coins):
    for beggar in range(count):
        outcome[beggar] += coins[index]
        index += 1
        if index == len(coins):
            break

print(outcome)
 
# nums = input().split(", ")
# count = int(input())
# outcome = [0] * count
#
# for i in range(len(nums)):
#     coin = int(nums[i])
#     index = i % count
#     outcome[index] += coin
#
# print(outcome)

# 1, 2, 3, 4, 5
# 2
# 100, 94, 24, 99
# 5
