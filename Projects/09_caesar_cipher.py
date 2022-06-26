alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(user_inserted, shift_number):
    encrypted_text = ""
    for char in user_inserted:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = pos + shift_number
            encrypted_text += alphabet[new_pos]
        else:
            encrypted_text += char
    print(f"Here's the encoded text: {encrypted_text}")

def decode(user_inserted, shift_number):
    decrypted_text = ""
    for char in user_inserted:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = pos - shift_number
            decrypted_text += alphabet[new_pos]
        else:
            decrypted_text += char
    print(f"Here's the encoded text: {decrypted_text}")

choice = input("Type 'encode' to encrypt or type 'decode' to decrypt: ")
message = input("Type your message: ")
shift = int(input("Insert the shift number: "))

if choice == "encode":
    encode(message, shift)
else:
    decode(message, shift)
