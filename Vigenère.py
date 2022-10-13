OUTPUT_RANGE = 127

def validate_upper_case_string(input, type):
    for chr in input:
        if (chr < 'A' or chr > 'Z'):
            raise Exception(f"Only Upper Case Alphabet are allowed in {type}.")

def validate_input(plain_text):
    validate_upper_case_string(plain_text, "Plain Text")
    if not plain_text:
        raise Exception("Plain Text can't be empty.")

def validate_key(key):
    validate_upper_case_string(key, "Key")
    if not key or len(key)>3:
        raise Exception("Length of key should be in range of 1-3.")

def extend_key(key, plain_text):
    """
        Makes Key same length as input by appending 
    """                                  
    input_size, key_size = len(plain_text), len(key)
    times, remaining = input_size//key_size, input_size%key_size
    return key*times + key[:remaining]

def encrypt(plain_text, key):
    """
        Return Encrypted string with range of whole ASCII
    """
    cipher_text = ""
    for pt, k in zip(plain_text, key):
        ascii_value = (ord(pt) + ord(k))%OUTPUT_RANGE
        cipher_text += chr(ascii_value)
    return cipher_text

if __name__ == "__main__": 
    plain_text = input("Enter the message to encrypted: ")
    validate_input(plain_text)
    key = input("Enter the key for Encryption: ")
    validate_key(key)
    
    key = extend_key(key, plain_text)
    cipher_text = encrypt(plain_text, key)
    
    print(f"Plain Text : {plain_text}")
    print(f"Extended Key : {key}")
    print(f"Cipher Text (ASCII Values) : {list(cipher_text.encode('ascii'))}")
    print(f"Cipher Text (Char Values): {cipher_text}")
    