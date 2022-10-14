def validate_upper_case_string(input, type):
    for chr in input:
        if (chr < 'A' or chr > 'Z'):
            raise Exception(f"Only Upper Case Alphabet are allowed in {type}.")

def validate_input(input, type):
    validate_upper_case_string(input, type)
    if not input:
        raise Exception(f"{type} can't be empty.")

def validate_vigenere_key(key):
    validate_upper_case_string(key, "Key")
    if not key or len(key)>3:
        raise Exception("Length of key should be in range of 1-3.")
