import Validator, VigenèreCipher

def main():
    plain_text = input("Enter the message to encrypted: ")
    Validator.validate_input(plain_text, "Plain Text")
    
    key = input("Enter the key for Encryption: ")
    Validator.validate_vigenere_key(key)
    
    key = VigenèreCipher.extend_key(key, plain_text)
    cipher_text = VigenèreCipher.encrypt(plain_text, key, 0, 127)
    
    print(f"Plain Text : {plain_text}")
    print(f"Extended Key : {key}")
    print(f"Cipher Text (ASCII Values) : {list(cipher_text.encode('ascii'))}")
    print(f"Cipher Text (Char Values): {cipher_text}")

if __name__ == "__main__": 
    main()