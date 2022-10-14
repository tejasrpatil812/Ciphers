
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(plaintext, key):
    cyphertext = ""
    validate_text(plaintext)
        
    for c in plaintext:
        cypherIndex = (alphabet.find(c) + key) % 26
        cyphertext += alphabet[cypherIndex]
        
    return cyphertext

def decrypt( cyphertext, key):
    return encrypt(cyphertext, 26 - key)

def validate_text(text):
    validate_upper_case_string(text)
    if not text:
        raise Exception("Plain Text can't be empty.")


def validate_upper_case_string(input):
    for chr in input:
        if (chr < 'A' or chr > 'Z'):
            raise Exception("Only Upper Case Alphabet are allowed.")
