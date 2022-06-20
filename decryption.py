import assets

alphabets = assets.alphabetLoad()

#encrypted_text = input('Encrypted Text: ')
encrypted_text = '''#%Ò5ÒÙûô+5ÒÙû[NÒÙû[Òô[ÒÙû[NÒÙû[Ò_[Òì5bûôÚ[uÒUÒ7%ôÚ5Û[Ò5ê9%Ò5ÒÙûô+5ÒÙû[ÛNÒREÒ_[Ò9[Û[ô_[NÒÙû[ô_5Ò7%pÒÙ[Û[ÛuÒúR%ÒÙû[ÒÁê%Ò7[!%ÒÙû[ÛNÒp[7ÒÙû[ÒÙ[Û[ÒìÚ[p[ÛÒ5ÒÙûô+5ÒÁê%ÒÙû[9[Ò_5Ò5ê+Û5ÒR[_5Ò_[Òì[7[u'''
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