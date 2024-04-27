alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(input_text, shift_amount, input_direction):
    output_text = ""
    
    if input_direction == "encode":
        for letter in input_text:
            if letter in alphabet:
                index = alphabet.index(letter)
                if index + shift_amount > 25:
                    index = index + shift_amount - 26
                else:
                    index = index + shift_amount
                output_text += alphabet[index]
            else:
                output_text += letter
        print(f"The encoded text is {output_text}")

    elif input_direction == "decode":
        for letter in input_text:
            if letter in alphabet:
                index = alphabet.index(letter)
                if index - shift_amount < 0:
                    index = index - shift_amount + 26
                else:
                    index = index - shift_amount
                output_text += alphabet[index]
            else:
                output_text += letter
        print(f"The decoded text is {output_text}")

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceasar(input_text=text, shift_amount=shift, input_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")