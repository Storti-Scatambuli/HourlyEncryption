with open('alphabets.txt', 'r') as arq:
    alphabets = arq.readlines()
    
for index, alphabet in enumerate(alphabets):
    alphabet = alphabet.split('"')
    alphabet[1] = alphabet[1][:len(alphabet[1])-1]
    alphabets[index] = alphabet
