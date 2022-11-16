alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    encoded_text = ''
    for i in text:
        next_index = alphabet.index(i) + shift
        if next_index > len(alphabet) - 1:
            encoded_text += alphabet[next_index - len(alphabet)]
        else:
            encoded_text += alphabet[next_index]
    print(encoded_text)


def decrypt(text, shift):
    decoded_text = ''
    for i in text:
        next_index = alphabet.index(i) - shift
        if next_index < 0:
            decoded_text += alphabet[next_index + len(alphabet)]
        else:
            decoded_text += alphabet[next_index]
    print(decoded_text)


if direction == 'encode':
    encrypt(text=text, shift=shift)
if direction == 'decode':
    decrypt(text=text, shift=shift)
