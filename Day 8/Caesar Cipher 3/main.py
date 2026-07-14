from art import logo

keep_running = True
# TODO-1: Import and print the logo from art.py when the program starts.
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?

def caesar(encode_or_decode, input_text, shift_amount):
    if encode_or_decode == 'decode':
        shift_amount *= -1

    output_text = ""
    for letter in input_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# TODO-3: Can you figure out a way to restart the cipher program?

while keep_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)

    go_again = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n").lower()
    if go_again == "no":
        print("Goodbye!")
        keep_running = False



