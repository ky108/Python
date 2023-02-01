while True:
    line = input()
    result = ''
    if line == 'End':
        break
    if line == 'SoftUni':
        continue

    for _ in line:
        result += _*2
    print(result)
