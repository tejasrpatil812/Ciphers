import Validator, VigenèreCipher

def write_file(file_name, data):
    with open(f'{file_name}.txt', 'w') as file:
        file.write(f"Total : {len(data)}\n")
        for d in data:
            file.write(f"{d}\n")

def extract_key():
    plain_text = input("Enter Plain Text : ")
    Validator.validate_input(plain_text, "Plain Text")

    cipher_text = input("Enter Cipher Text : ")
    Validator.validate_input(cipher_text, "Cipher Text")
    
    generated_extended_key, generated_key = VigenèreCipher.reverse_generate_key(plain_text, cipher_text)
    seached_key, total_keys = VigenèreCipher.exhaustive_key_search(plain_text, cipher_text)

    print(f"Extracted Key {generated_key} out of Reverse Generated Extended Key : {generated_extended_key}")
    
    print(f"Found Exhaustive Searched Key : [ {seached_key} ] after {len(total_keys)} keys")
    write_file(f"generated_keys_for_{plain_text}", total_keys)


def main():
    while(True):
        print("\n------------------------------------------------------\n")
        print("1. Extract Key \n2. Exit\n")
        try:
            choice = int(input("Enter choice: "))
        except:
            print("Invalid choice. Try Again!")
            continue
        
        try:
            if choice == 1:
                extract_key()
            else:
                break
        except Exception as e:
            print(e)

if __name__ == "__main__": 
    main()