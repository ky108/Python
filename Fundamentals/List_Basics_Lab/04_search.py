n = int(input())
positive = []
negative = []
for _ in range(n):
    num = int(input())
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

print(f"{positive}\n"
      f"{negative}\n"
      f"Count of positives: {len(positive)}\n"
      f"Sum of negatives: {sum(negative)}")

# 6
# 11
# 2
# 35
# 599
# 31
# 20
