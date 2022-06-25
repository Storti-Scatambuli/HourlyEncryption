import assets

alphabets = assets.alphabetLoad()


encrypted_text = '''RQepIVwàì'''
key = '10:235959'.split(':')
encrypted_text = list(encrypted_text)

alphabet_cryptography = assets.alphabetFind(alphabets, key)

for index_text, character in enumerate(encrypted_text):
    if character == '\n' or character == '§' or character == '₢' or character == '"':
        continue
    character_alphabet_index = alphabet_cryptography.index(character)
    index_criptography = character_alphabet_index
    full_sweep = int(key[0]) + index_text
    for _ in range(full_sweep):
        if index_criptography < 0:
            index_criptography = len(alphabet_cryptography)-1
        index_criptography -= 1    
    encrypted_text[index_text] = alphabet_cryptography[index_criptography]

dec = ''.join(encrypted_text)
print(dec)