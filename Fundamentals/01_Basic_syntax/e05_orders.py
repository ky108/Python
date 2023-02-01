orders = int(input())
total = 0
for _ in range(orders):
    price_capsule = float(input())
    days = int(input())
    per_day = int(input())
    if price_capsule < 0.01 or price_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if per_day < 1 or per_day > 2000:
        continue

    orders_price = days * price_capsule * per_day
    total += orders_price
    print(f"The price for the coffee is: ${orders_price:.2f}")

print(f'Total: ${total:.2f}')

# 2
# 9.223
# 31
# 0
# 0.05
# 10
# 30