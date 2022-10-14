import Validator
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(plaintext, key):
    cyphertext = ""
    Validator.validate_input(plaintext, "Plain Text")
        
    for c in plaintext:
        cypherIndex = (alphabet.find(c) + key) % 26
        cyphertext += alphabet[cypherIndex]
        
    return cyphertext

def decrypt( cyphertext, key):
    return encrypt(cyphertext, 26 - key)
