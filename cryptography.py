import time
import assets

alphabets = assets.alphabetLoad()
hour = f'{time.localtime().tm_hour}'.zfill(2)
minute = f'{time.localtime().tm_min}'.zfill(2)
second = f'{time.localtime().tm_sec}'.zfill(2)
key_time = f'{hour}{minute}{second}'

key_time_test = '000000'

text = 'Your Text'

key_criptography = f'48:{key_time_test}'.split(':')

text_list = list(text)

#Código em construção x_x_x_x
for criptography in alphabets:
    if criptography[0] == key_criptography[1]:
        alphabet_criptography = criptography[1]
        break

for index, caracter in enumerate(text_list):
    caracter_alfabeto_indice = alphabet_criptography.index(caracter)
    soma = index + int(key_criptography[0]) + caracter_alfabeto_indice
    if soma >= len(alphabet_criptography):
        soma = len(alphabet_criptography) - soma
    text_list[index] = alphabet_criptography[soma]
    
    
texto_criptografado = ''.join(text_list)
print(texto_criptografado, key_criptography)