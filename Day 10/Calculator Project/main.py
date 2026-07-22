from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# print(calculation["*"](4, 8))

# Add the logo from art.py
print(logo)



def calculator():
    should_accumulate = True
    valid_operation = False

    # Program asks the user to type the first number.
    first_number = float(input("What's the first number?: "))

    while should_accumulate:
        for symbol in calculation:
            print(symbol)

        # Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
        while not valid_operation:
            operation = input("Pick an operation: ")
            if operation in calculation:
                valid_operation = True
            else:
                print("Invalid operation, please try again")

    # Program asks the user to type the second number.
        next_number = float(input("What's the next number?: "))

    # Program works out the result based on the chosen mathematical operator.
        result = calculation[operation](first_number, next_number)
        print(f"{first_number} {operation} {next_number} = {result}")

    # Program asks if the user wants to continue working with the previous result.
        valid_operation = False
        continue_calculating = input(
            f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: "
        ).lower()
        if continue_calculating == 'n':
            should_accumulate = False
            calculator()
        elif continue_calculating == 'y':
            first_number = result
        else:
            should_accumulate = False
            print("Thanks for using the calculator! Goodbye!")

    # If yes, program loops to use the previous result as the first number and then repeats the calculation process.
    # If no, program asks the user for the fist number again and wipes all memory of previous calculations.

calculator()
