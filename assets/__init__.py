def alphabetGenerate(alphabetsfile='alphabets/alphabets.txt'):
    import random
    
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÇabcdefghijklmnopqrstuvwxyzçÁÀÃÂÉÊÈÍÎÌÓÒÕÔÚÙÛáàãâéèêíîìóòõôúû1234567890,.;:/?][}{-_=+!@#$%&*() ºª°'
    alphabet = list(alfabeto)

    for h in range(0, 24):
        for m in range(0, 60):
            for s in range(0, 60):
                aleatorio = random.sample(alphabet, len(alphabet))
                text = ''.join(aleatorio)
                with open(alphabetsfile, 'a') as arq:
                    hour = str(h).zfill(2)
                    minute = str(m).zfill(2)
                    second = str(s).zfill(2)
                    arq.write(f'{hour}{minute}{second}"{text}\n')
                print(h, m, s)
                
def alphabetVerification(alphabetsfile='alphabets/alphabets.txt'):
        
    with open(alphabetsfile, 'r') as arq:
        alphabetslist = arq.readlines() 
    for index, alphabet in enumerate(alphabetslist):
        alphabet = alphabet.split('"')
        alphabet[1] = list(alphabet[1][:len(alphabet[1])-1])
        alphabetslist[index] = alphabet
        
    alphabetslist2 = alphabetslist.copy()
    
    same_occurrences = {'Alphabets': [], 'Quantity': 0}
    for index, alphabet in enumerate(alphabetslist):
        print(f'{index+1}/{len(alphabetslist)}')
        for index2, alphabet2 in enumerate(alphabetslist2):
            if index2 != index:
                if alphabet == alphabet2:
                    registred = False
                    for index_same_occurrences in same_occurrences['Alphabets']:
                        if index_same_occurrences == index:
                            registred == True
                    if not registred:
                        same_occurrences['Alphabets'].append(index)
                        same_occurrences['Quantity'] += 1
    print(same_occurrences)
    
if __name__ == '__main__':
    print(f'{"1":.<40}Alphabet Generate')
    print(f'{"2":.<40}Alphabet Verification')
    try:
        entry = int(input())
    except ValueError:
        print('Enter an integer value')
    else:
        if entry == 1:
            alphabetGenerate()
        elif entry == 2:
            alphabetVerification()