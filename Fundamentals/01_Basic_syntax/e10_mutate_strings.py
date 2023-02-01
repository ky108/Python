a = input()
b = input()
for i in range(len(a)):
    # temp = b[0:i + 1] + a[i + 1:len(a) + 1]

    temp = b[: i + 1] + a[i + 1:]
    if a[i] != b[i]:
        print(temp)

# bubble gum
# turtle hum
