# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
# greet_with_name("Jack Bauer")

def life_in_weeks(age):
    age_in_weeks = age * 52
    print(f"You have {4680 - age_in_weeks} weeks left.")

life_in_weeks(56)

# def greet_with(name, location):
#     print(f"Hello {name}, how is it in {location}?")
#
# user_name = input("What is your name? ")
# user_location = input("Where do you live? ")
# greet_with(user_name, user_location)

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with(location="London", name="John")

def calculate_love_score(name1, name2):
    love_score = 0
    names = (name1+name2).upper()

    for letter in names:
        for char in "TRUE":
            if letter == char:
                love_score += 10
        for char in "LOVE":
            if letter == char:
                love_score += 1

    print(love_score)
