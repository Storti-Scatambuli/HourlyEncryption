def alphabetGenerate():
    import random
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÇabcdefghijklmnopqrstuvwxyzçÁÀÃÂÉÊÈÍÎÌÓÒÕÔÚÙÛáàãâéèêíîìóòõôúû1234567890,.;:/?][}{-_=+!@#$%&*() '

    alphabet = list(alfabeto)

    alphabets = []


    for h in range(0, 24):
        for m in range(0, 60):
            for s in range(0, 60):
                aleatorio = random.sample(alphabet, len(alphabet))
                text = ''.join(aleatorio)
                with open('alphabets.txt', 'a') as arq:
                    hour = str(h).zfill(2)
                    minute = str(m).zfill(2)
                    second = str(s).zfill(2)
                    arq.write(f'{hour}{minute}{second}"{text}\n')

def alphabetLoad():
    with open('alphabets.txt', 'r') as arq:
        alphabets = arq.readlines()
        
    for index, alphabet in enumerate(alphabets):
        alphabet = alphabet.split('"')
        alphabet[1] = list(alphabet[1][:len(alphabet[1])-1])
        alphabets[index] = alphabet
    return alphabets

def alphabetFind(alphabets, key_criptography):
    alphabet_criptography = []
    for criptography in alphabets:
        if criptography[0] == key_criptography[1]:
            alphabet_criptography = criptography[1]
            break
    if len(alphabet_criptography) == 0:
        print('Alphabet not find')
        return None
    else:
        return alphabet_criptography