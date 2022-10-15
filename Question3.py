import Validator, VigenèreCipher

def encrypt():
    plain_text = input("Enter the message to be encrypted: ")
    Validator.validate_input(plain_text, "Plain Text")
    
    key = input("Enter the key for Encryption: ")
    Validator.validate_vigenere_key(key)
    
    key = VigenèreCipher.extend_key(key, plain_text)
    cipher_text = VigenèreCipher.encrypt(plain_text, key, 0, 127)
    cipher_text_ascii = cipher_text.encode('ascii')
    
    print(f"Plain Text : {plain_text}")
    print(f"Extended Key : {key}")
    print(f"Cipher Text (HEX Values) : {cipher_text_ascii.hex()}")
    print(f"Cipher Text (ASCII Values) : {list(cipher_text_ascii)}")
    print(f"Cipher Text (Char Values): {cipher_text}")

def decrypt():
    cipher_hex = input("Enter the message to be decrypted (HEX String): ")
    Validator.validate_hex_input(cipher_hex, "Cipher Text")

    key = input("Enter the key for Decryption: ")
    Validator.validate_vigenere_key(key)
    
    cipher_ascii = bytes.fromhex(cipher_hex)
    key = VigenèreCipher.extend_key(key, cipher_ascii)
    
    plain_text = VigenèreCipher.decrypt(cipher_ascii, key, 0, 127)
    print(f"Decrypted Plain Text : {plain_text}")


def main():
    while(True):
        print("------------------------------------------------------\n")
        print("1. Encrypt \n2. Decypt \n3. Exit\n")
        try:
            choice = int(input("Enter choice: "))
        except:
            print("Invalid choice. Try Again!")
            continue
        try:
            if choice == 1:
                encrypt()
            elif choice == 2:
                decrypt()
            else:
                break
        except Exception as e:
            print(e)

if __name__ == "__main__": 
    main()