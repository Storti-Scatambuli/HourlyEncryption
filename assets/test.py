import time

hora = f'{time.localtime().tm_hour}{time.localtime().tm_min}{time.localtime().tm_sec}'

texto = 'Hello World'

chave = f'3:{hora}'.split(':')

texto_lista = list(texto)

#Código em construção x_x_x_x
for criptografia in alphabets:
    if criptografia[0] == chave[1]:
        alfabeto_criptografia = criptografia[1]
        break

for index, caracter in enumerate(texto_lista):
    caracter_alfabeto_indice = alfabeto_criptografia.index(caracter)
    soma = index + int(chave[0]) + caracter_alfabeto_indice
    if soma >= len(alfabeto_criptografia):
        soma = alfabeto_criptografia - soma
    texto_lista[index] = alfabeto_criptografia[soma]
    
    
texto_criptografado = ''.join(texto_lista)
print(texto_criptografado, chave)
