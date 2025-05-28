print ("""
   _____                            _____ _       _               
  / ____|                          / ____| |     (_)              
 | |     __ _ ___  ___ ___  ___  | |    | |_   _ _ _ __ ___  ___ 
 | |    / _` / __|/ __/ _ \/ __| | |    | | | | | | '__/ _ \/ __|
 | |___| (_| \__ \ (_| (_) \__ \ | |____| | |_| | | | |  __/\__ /
  \_____\__,_|___/\___\___/|___/  \_____|_|\__,_|_|_|  \___||___/
                                                                 

""")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1  # reverse the shift for decoding
    
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
