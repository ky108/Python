budget = int(input())

product = input()
while product != 'End':
        price = int(product)

        budget -= price
        if budget < 0:
            print('You went in overdraft!')
            exit()
        product = input()

print('You bought everything needed.')


# 100
# 5
# End
