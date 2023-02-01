budget = float(input())
kg_flour = float(input())   # 1 loaf = Eggs 1 pack + Flour 1kg + Milk 0.250l
eggs = kg_flour * 0.75
milk = kg_flour * 1.25      # 250ml milk for a bread
colored = 0
loaves = 0
while budget >= 0:
    one_bread = eggs + kg_flour + milk * 0.25
    if budget - one_bread < 0:
        break
    else:
        budget -= one_bread
        colored += 3
        loaves += 1
        if loaves % 3 == 0:
            colored -= loaves - 2
            if colored < 0:
                break

print(f'You made {loaves} loaves of Easter bread! '
      f'Now you have {colored} eggs and {budget:.2f}BGN left.')
