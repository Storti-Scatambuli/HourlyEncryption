import time
import assets

alphabets = assets.alphabetLoad()
hour = f'{time.localtime().tm_hour}'.zfill(2)
minute = f'{time.localtime().tm_min}'.zfill(2)
second = f'{time.localtime().tm_sec}'.zfill(2)
key_time = f'{hour}{minute}{second}'

key_time_test = '000000'

text = '''Se o pinto pia, pia na pia, pia da cozinha. A senhora ouve o pinto piar, lá da varanda, piando sem parar. Ele pia que sabe piar, mas pia para chamar o pinto que piava do outro lado da casa.'''

key_cryptography = f'9:{key_time_test}'.split(':')

text_list = list(text)


alphabet_cryptography = assets.alphabetFind(alphabets, key_cryptography)

for index_text, character in enumerate(text_list):
    if character == '\n' or character == 'º' or character == '-':
        continue
    character_alphabet_index = alphabet_cryptography.index(character)
    index_cryptography = character_alphabet_index
    for _ in range(int(key_cryptography[0])):
        index_cryptography += 1
        if index_cryptography >= len(alphabet_cryptography):
            index_cryptography = 0
    text_list[index_text] = alphabet_cryptography[index_cryptography]
    
    
texto_criptografado = ''.join(text_list)
print(texto_criptografado, key_cryptography)