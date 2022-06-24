letters = ' abcdefghijklmnopqrstuvwxyz'


def treat_letter_index(letter_index):
    if letter_index < 0:
        letter_index = len(letters) + letter_index
        
    if letter_index >= len(letters):
        letter_index = letter_index - len(letters)
        

    return letter_index


def encrypt(key, message):
    message += ' ' * (len(message) % len(key) + 1)

    encrypted_message = ''
    key_index = 0
    for letter in message.lower():
        encrypted_letter_index = letters.find(letter) + key[key_index]
        encrypted_message += letters[treat_letter_index(encrypted_letter_index)]

        key_index += 1
        if key_index >= len(key):
            key_index = 0

    return encrypted_message


def decrypt(key, message):
    decrypted_message = ''
    key_index = 0
    for letter in message.lower():
        decrypted_letter_index = letters.find(letter) - key[key_index]
        decrypted_message += letters[treat_letter_index(decrypted_letter_index)]

        key_index += 1
        if key_index >= len(key):
            key_index = 0

    return decrypted_message

options = {
    'E': encrypt,
    'D': decrypt
}

option = 'E'
while option in options:
    message = input("Informe a mensagem: ")
    key = [int(key_item) for key_item in input("Informe a chave separando por espaços: ").split(" ")]
    option = input("O que deseja fazer? (E) - Encriptar | (D) - Decriptar \nPara sair, basta apertar qualquer outro botão\n")
    option = option.upper()

    if option in options:
        print(options[option](key, message))
