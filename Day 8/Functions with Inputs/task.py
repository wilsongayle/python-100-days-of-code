def greet():
    print("Hello World")
    print("Hello Galaxy")
    print("Hello Universe")

greet()

def greet_user(name):
    print(f"Hello {name}")

user_name = input("What is your name? ")
greet_user(user_name)