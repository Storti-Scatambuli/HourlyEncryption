class HourlyEncryption():
    plain_text = ''
    primary_key = 0
    hour_key = '000000'
    alphabetslist = []
    
    def __init__(self, alphabetfile='alphabets.txt'):
        self.alphabetfile = alphabetfile
        
        with open('alphabets.txt', 'r') as arq:
            self.alphabetslist = arq.readlines()
        
        for index, alphabet in enumerate(self.alphabetslist):
            alphabet = alphabet.split('"')
            alphabet[1] = list(alphabet[1][:len(alphabet[1])-1])
            self.alphabetslist[index] = alphabet
