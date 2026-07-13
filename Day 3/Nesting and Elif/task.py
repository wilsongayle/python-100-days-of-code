print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    price = 0
    if age > 18:
        print("Adult tickets are $12")
        price = 12
    elif age >= 12:
        print("Youth tickets are $7")
        price = 7
    else:
        print("Child tickets are $5")
        price = 5

    photo = input("Do you want a photo? (Y/N) ")
    if photo == "Y" or photo == "y":
        price += 3

    print(f"Your total cost is ${price}")
else:
    print("Sorry you have to grow taller before you can ride.")
