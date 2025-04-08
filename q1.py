import string 
from collections import Counter
class RepeatedKeyCipher:

    def __init__(self, key: bytes = bytes([0, 0, 0, 0, 0])):
        """Initializes the object with a list of integers between 0 and 255."""
        # WARNING: DON'T EDIT THIS FUNCTION!
        self.key = list(key)

    def encrypt(self, plaintext: str) -> bytes:
        """Encrypts a given plaintext string and returns the ciphertext."""
        # TODO: IMPLEMENT THIS FUNCTION
 
        byte_array = plaintext.encode('latin-1')
        encrypted_array = []
        key_index = 0

        for _ in range(len(byte_array)):
            if _%len(self.key) == 0:
                key_index = -1; 
            key_index += 1
            encrypted_array.append(byte_array[_] ^ self.key[key_index])
            
        return bytes(encrypted_array) 
            

    def decrypt(self, ciphertext: bytes) -> str:
        """Decrypts a given ciphertext string and returns the plaintext."""
        byte_array = ciphertext.decode('latin-1')
        decrypt_bytes = self.encrypt(byte_array)
        return decrypt_bytes.decode('latin-1')


class BreakerAssistant:

    def plaintext_score(self, plaintext: str) -> float:
        """Scores a candidate plaintext string, higher means more likely."""
        # Please don't return complex numbers, that would be just annoying.
        # TODO: IMPLEMENT THIS FUNCTION
        score = 0
        for char in plaintext:
            if char == ' ':
                score += 10
            elif char in string.ascii_letters:
                score += 3
            elif char in string.digits:
                score += 1
        return score
        
    def generateKeys(self,length,current_key=b'',all_keys=None):
        if all_keys is None:
            all_keys = []
        
        if length == 0:
            all_keys.append(current_key)
            return all_keys
        
        for i in range(256):
            self.generateKeys(length-1,current_key + bytes([i]),all_keys)
            
        return all_keys
    
    def brute_force(self, cipher_text: bytes, key_length: int) -> str:
        """Breaks a Repeated Key Cipher by brute-forcing all keys."""
        # TODO: IMPLEMENT THIS FUNCTION
        best_plaintext = ""
        best_score = -1
        all_keys = self.generateKeys(key_length)
        
        for key in all_keys:
            current_cipher = RepeatedKeyCipher(key)
            current_plaintext = current_cipher.decrypt(cipher_text)
            current_score = self.plaintext_score(current_plaintext)

            if current_score > best_score:

                best_score = current_score
                best_plaintext = current_plaintext
                
        return best_plaintext

    def smarter_break(self, cipher_text: bytes, key_length: int) -> str:
        """Breaks a Repeated Key Cipher any way you like."""
        # TODO: IMPLEMENT THIS FUNCTION
        key = bytearray(key_length)
        
        for i in range(key_length):
            subciphertext = cipher_text[i::key_length]
            best_byte = 0
            max_score = 0
            
            for b in range(256):
                dectypted_segment = bytearray()
                for byte in subciphertext:
                    dectypted_segment.append(byte ^ b)
                    
                dectypted_text = dectypted_segment.decode('latin-1')
                score = self.plaintext_score(dectypted_text)
                
                if score > max_score:
                    max_score = score
                    best_byte = b
                    
            key[i] = best_byte
            
        final_key = bytearray(key)
        cliper = RepeatedKeyCipher(final_key)
        plaintext = cliper.decrypt(cipher_text)
        
        return plaintext
        

