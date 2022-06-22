import time
import assets

alphabets = assets.alphabetLoad()
hour = f'{time.localtime().tm_hour}'.zfill(2)
minute = f'{time.localtime().tm_min}'.zfill(2)
second = f'{time.localtime().tm_sec}'.zfill(2)
key_time = f'{hour}{minute}{second}'

key_time_test = '000000'

text = '''Aaaaaaaa'''

key_cryptography = f'9:{key_time}'.split(':')

text_list = list(text)


alphabet_cryptography = assets.alphabetFind(alphabets, key_cryptography)

for index_text, character in enumerate(text_list):
    if character == '\n' or character == '§' or character == '₢':
        continue
    character_alphabet_index = alphabet_cryptography.index(character)
    index_cryptography = character_alphabet_index
    full_sweep = int(key_cryptography[0]) + index_text
    for _ in range(full_sweep):
        index_cryptography += 1
        if index_cryptography >= len(alphabet_cryptography):
            index_cryptography = 0
    text_list[index_text] = alphabet_cryptography[index_cryptography]
    
    
texto_criptografado = ''.join(text_list)
print(texto_criptografado, key_cryptography)