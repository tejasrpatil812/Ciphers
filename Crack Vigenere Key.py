def validate_upper_case_chars(input, type):
    for chr in input:
        if (chr < 'A' or chr > 'Z'):
            raise Exception(f"Only Upper Case Alphabet are allowed in {type}.")

def extend_key(key, plain_text):
    """
        Makes Key same length as input by appending itself
    """                                  
    input_size, key_size = len(plain_text), len(key)
    times, remaining = input_size//key_size, input_size%key_size
    return key*times + key[:remaining]

if __name__ == "__main__": 
    plain_text = input("Enter Plain Text : ")
    validate_upper_case_chars(plain_text, "Plain Text")

    cipher_text = input("Enter Cipher Text : ")
    validate_upper_case_chars(cipher_text, "Cypher Text")
    
    key=""
    for pt, ct in zip(plain_text, cipher_text):
        ascii_value = ord('A') + (ord(ct)+26-ord(pt))%26
        key+=chr(ascii_value)
        
    keys = []
    for i in range(1,4):
        # Check whether key size of 1-3 recreates extracted extended key
        generated_key = extend_key(key[:i], plain_text)
        if generated_key == key:
            keys.append(key[:i])
        
    print(f"Plain Text : {plain_text}")
    print(f"Cipher Text : {cipher_text}")
    print(f"Extracted Extended Key : {key}")
    print(f"Extracted Keys : {keys}")