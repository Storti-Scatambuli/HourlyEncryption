class HourlyEncryption():
    
    def __init__(self, plaintext, alphabetfile='alphabets/alphabets.txt'):    
        self.plain_text = list(plaintext)
        self.final_text = self.plain_text.copy()
        self.key_cryptography = [0, '000000']
        self.alphabetslist = []
        self.alphabetfile = alphabetfile
        
        with open(self.alphabetfile, 'r') as arq:
            self.alphabetslist = arq.readlines()
        
        for index, alphabet in enumerate(self.alphabetslist):
            alphabet = alphabet.split('"')
            alphabet[1] = list(alphabet[1][:len(alphabet[1])-1])
            self.alphabetslist[index] = alphabet

    def alphabetFind(self):
        
        for cryptography in self.alphabetslist:
            if cryptography[0] == self.key_cryptography[1]:
                return cryptography[1]
    
    def cryptography(self, primarykey):
        
        from time import localtime
        
        hour = f'{localtime().tm_hour}'.zfill(2)
        minute = f'{localtime().tm_min}'.zfill(2)
        second = f'{localtime().tm_sec}'.zfill(2)
        secudarykey = f'{hour}{minute}{second}'
        self.key_cryptography = [primarykey, secudarykey]
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
            self.final_text[index_text] = self.alphabet_cryptography[index_cryptography]
        self.final_text = ''.join(self.final_text)

    def decryption(self, primarykey, secundarykey):
        
        self.key_cryptography = [primarykey, str(secundarykey)]
        alphabet_cryptography = self.alphabetFind()

        for index_text, character in enumerate(self.plain_text):
            if character == '\n' or character == '§' or character == '₢' or character == '"':
                continue
            character_alphabet_index = alphabet_cryptography.index(character)
            index_criptography = character_alphabet_index
            full_sweep = int(self.key_cryptography[0]) + index_text
            for _ in range(full_sweep):
                if index_criptography < 0:
                    index_criptography = len(alphabet_cryptography)-1
                index_criptography -= 1    
            self.final_text[index_text] = alphabet_cryptography[index_criptography]
        self.final_text = ''.join(self.final_text)
            
    

if __name__ == '__main__':
    
    example_text_decrypt = 'Your Text'
    example_key = 23
    encrypt = HourlyEncryption(example_text_decrypt)
    encrypt.cryptography(example_key)
    print(encrypt.final_text)
    print(encrypt.key_cryptography)
    
    example_text_encrypt = 'Nil-aJiZª'
    decrypt = HourlyEncryption(example_text_encrypt)
    decrypt.decryption(23, 224101)
    print(decrypt.final_text)
    
    