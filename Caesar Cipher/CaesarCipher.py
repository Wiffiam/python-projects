#Caesar cipher decryption and encryption algorithm
#September 29, 2021
#William Wu

from CaesarArt import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

continue_program = True

def caesar(plain_text, shift_amount, encode_direction):
    cipher_text = ""
    if encode_direction == "decode":
        shift_amount *= -1
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position >= 26:
                new_position -= 26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else: cipher_text += char
    print(f"Your new text is {cipher_text}")

while continue_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift >= 26:
        shift = shift % 26

    caesar(plain_text=text, shift_amount=shift, encode_direction=direction)
    user_continue = input("Would you like to continue? Type yes or no. \n")
    if user_continue == "yes":
        continue_program = True
    elif user_continue == "no":
        print("Goodbye!")
        continue_program = False