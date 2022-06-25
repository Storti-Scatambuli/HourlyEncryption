import time
import assets

alphabets = assets.alphabetLoad()
hour = f'{time.localtime().tm_hour}'.zfill(2)
minute = f'{time.localtime().tm_min}'.zfill(2)
second = f'{time.localtime().tm_sec}'.zfill(2)
key_time = f'{hour}{minute}{second}'

key_time_test = '235959'

text = '''Um dia descobrimos que beijar uma pessoa para esquecer outra é bobagem.
Você não só não esquece a outra pessoa como pensa muito mais nela...
Um dia nós percebemos que as mulheres têm instinto "caçador" e fazem qualquer homem sofrer...
Um dia descobrimos que se apaixonar é inevitável...
Um dia percebemos que as melhores provas de amor são as mais simples...
Um dia percebemos que o comum não nos atrai...
Um dia saberemos que ser classificado como "bonzinho" não é bom...
Um dia perceberemos que a pessoa que nunca te liga é a que mais pensa em você...
Um dia percebemos que somos muito importante para alguém, mas não damos valor a isso...
Um dia percebemos como aquele amigo faz falta, mas ai já é tarde demais...
Enfim...
Um dia descobrimos que apesar de viver quase um século esse tempo todo não é suficiente para realizarmos todos os nossos sonhos, para beijarmos todas as bocas que nos atraem, para dizer o que tem de ser dito...
O jeito é: ou nos conformamos com a falta de algumas coisas na nossa vida ou lutamos para realizar todas as nossas loucuras...'''

key_cryptography = f'9:{key_time}'.split(':')

text_list = list(text)


alphabet_cryptography = assets.alphabetFind(alphabets, key_cryptography)

for index_text, character in enumerate(text_list):
    if character == '\n' or character == '§' or character == '₢' or character == '"':
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