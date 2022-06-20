import assets

alphabets = assets.alphabetLoad()

encrypted_text = input('Encrypted Text: ')
encrypted_text_test = '''v5êÛÒS%&+'''
key = input('Key (number:time): ').split(':')
encrypted_text = list(encrypted_text)

alphabet_cryptography = assets.alphabetFind(alphabets, key)

for index_text, character in enumerate(encrypted_text):
    if character == '\n' or character == 'º':
        continue
    character_alphabet_index = alphabet_cryptography.index(character)
    index_criptography = character_alphabet_index
    for _ in range(int(key[0])):
        if index_criptography < 0:
            index_criptography = len(alphabet_cryptography)-1
        index_criptography -= 1    
    encrypted_text[index_text] = alphabet_cryptography[index_criptography]

dec = ''.join(encrypted_text)
print(dec)