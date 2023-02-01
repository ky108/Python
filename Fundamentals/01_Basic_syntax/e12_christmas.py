qty = int(input())
days = int(input())
orn_set = 2
skirt = 5
garland = 3
lights = 15

budget = 0
spirit = 0
for i in range(1, days + 1):
    if i % 11 == 0:
        qty += 2
    if i % 2 == 0:
        budget += orn_set * qty
        spirit += 5
    if i % 3 == 0:
        budget += (skirt + garland) * qty
        spirit += 3 + 10
    if i % 5 == 0:
        budget += lights * qty
        spirit += 17
        if i % 3 == 0:
            spirit += 30
    if i % 10 == 0:
        spirit -= 20
        budget += skirt + garland + lights
        if i == days:
            spirit -= 30
print(f'Total cost: {budget}\n'
      f'Total spirit: {spirit}')
