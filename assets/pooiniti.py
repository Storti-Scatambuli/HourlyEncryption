
class HourlyEncryption():   
    def __init__(self, plaintext, primarykey, alphabetfile='alphabets.txt'):
        
        self.plain_text = list(plaintext)
        self.key_cryptography = [primarykey, '000000']
        self.alphabetslist = []
        self.alphabetfile = alphabetfile
        
        with open('alphabets.txt', 'r') as arq:
            self.alphabetslist = arq.readlines()
        
        for index, alphabet in enumerate(self.alphabetslist):
            alphabet = alphabet.split('"')
            alphabet[1] = list(alphabet[1][:len(alphabet[1])-1])
            self.alphabetslist[index] = alphabet

    def alphabetFind(self):
        
        alphabet_criptography = []
        for cryptography in self.alphabetslist:
            if cryptography[0] == self.key_cryptography[1]:
                return cryptography[1]
    
    def cryptography(self):
        
        from time import localtime
        
        hour = f'{localtime().tm_hour}'.zfill(2)
        minute = f'{localtime().tm_min}'.zfill(2)
        second = f'{localtime().tm_sec}'.zfill(2)
        key_time = f'{hour}{minute}{second}'
        
        self.encrypted_text = self.plain_text.copy()
        self.key_cryptography[1] = key_time
        self.alphabet_cryptography = self.alphabetFind()
        
        for index_text, character in enumerate(self.plain_text):
            if character == '\n' or character == '§' or character == '₢' or character == '"':
                continue
            character_alphabet_index = self.alphabet_cryptography.index(character)
            index_cryptography = character_alphabet_index
            full_sweep = int(self.key_cryptography[0]) + index_text
            for _ in range(full_sweep):
                index_cryptography += 1
                if index_cryptography >= len(self.alphabet_cryptography):
                    index_cryptography = 0
            self.encrypted_text[index_text] = self.alphabet_cryptography[index_cryptography]
        self.encrypted_text = ''.join(self.encrypted_text)

    

if __name__ == '__main__':
    
    example_text = 'Your Text'
    example_key = 23
    encrypt = HourlyEncryption(example_text, example_key)
    encrypt.cryptography()
    print(encrypt.encrypted_text)
    print(encrypt.key_cryptography)
    