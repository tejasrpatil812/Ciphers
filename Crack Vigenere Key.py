def validate_input(input, type):
    if not input:
        raise Exception(f"{type} can't be empty.")
    for chr in input:
        if (chr < 'A' or chr > 'Z'):
            raise Exception(f"Only Upper Case Alphabet are allowed in {type}.")

def write_file(file_name, data):
    with open(f'{file_name}.txt', 'w') as file:
        file.write(f"Total : {len(data)}\n")
        for d in data:
            file.write(f"{d}\n")

def extend_key(key, plain_text):
    """
        Makes Key same length as input by appending itself
    """                                  
    input_size, key_size = len(plain_text), len(key)
    times, remaining = input_size//key_size, input_size%key_size
    return key*times + key[:remaining]

def encrypt(plain_text, key, start = ord('A'), range = 26):
    """
        Return Encrypted string using Vigenere Cipher
    """
    cipher_text = ""
    for pt, k in zip(plain_text, key):
        ascii_value = start + (ord(pt) + ord(k))%range
        cipher_text += chr(ascii_value)
    return cipher_text

def reverse_generate_key(plain_text, cipher_text):
    """
        Reverse generates key out of Plain Text and Cipher Text
    """
    extended_key=""
    for pt, ct in zip(plain_text, cipher_text):
        ascii_value = ord('A') + (ord(ct)+26-ord(pt))%26
        extended_key+=chr(ascii_value)
        
    keys = []
    for i in range(1,4):
        # Check whether key size of 1-3 recreates extracted extended key
        generated_key = extend_key(extended_key[:i], plain_text)
        if generated_key == extended_key:
            keys.append(extended_key[:i])
    return extended_key, keys
    
def is_valid_key(key, plain_text, cipher_text):
    extended_key = extend_key(key, plain_text)
    return encrypt(plain_text, extended_key) == cipher_text

def exhaustive_search_key(plain_text, cipher_text):
    """
        Exhaustive Searches Key with length 1-3 and which
        corresponds to given Plain Text and Cipher Text
    """
    keys = []
    key_set = [""]
    for _ in range(3):
        new_key_set = []
        for key in key_set:
            for i in range(26):
                current_key = key
                current_key+=chr(ord('A')+i)
                new_key_set.append(current_key)
                if is_valid_key(current_key, plain_text, cipher_text):
                    keys.extend(new_key_set)
                    return current_key, keys

        keys.extend(new_key_set)
        key_set = new_key_set
    return "", keys


if __name__ == "__main__": 
    plain_text = input("Enter Plain Text : ")
    validate_input(plain_text, "Plain Text")

    cipher_text = input("Enter Cipher Text : ")
    validate_input(cipher_text, "Cypher Text")
    
    generated_extended_key, generated_key = reverse_generate_key(plain_text, cipher_text)
    
    seached_key, total_keys = exhaustive_search_key(plain_text, cipher_text)
    write_file("generated_keys", total_keys)

    print(f"Extracted Key {generated_key} out of Reverse Generated Extended Key : {generated_extended_key}")
    print(f"Exhaustive Searched Key : {seached_key}")