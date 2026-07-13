total = 0

for num in range(1,101):
    total += num

print(total)

for num in range(1, 101):
    value = ''
    if(num % 3 == 0):
        value += "Fizz"
    if(num % 5 == 0):
        value += "Buzz"
    if value == '':
        print(num)
    else:
        print(value)