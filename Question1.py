import CaesarCipher

tries = 3

def main():
    key = 0
    for i in range(tries):
        try:
            key = int(input("Enter the key for the Cipher: "))
            break
        except:
            if i < tries - 1 : 
                print("\nExpecting int value for key. Try Again! Attempts left: ", str(tries - 1 -i))
                continue
            else:
                print("\nExpecting int value for key. Exhausted {0} attemps. Exiting!".format(tries))

    if key < 0 or key >= 26:
        print("Exiting! The key {0} is invalid.".format(key))
        return

    exit = False
    while(not exit):
        print("\n1. Print the cipher mapping 2. Encrypt 3. Decypt 4. Exit")
        try:
            choice = int(input("Enter choice: "))
        except:
            print("\nInvalid choice. Try Again!")
            continue
        if choice == 1:
            printMapping(key)
        elif choice == 2:
            text = input("Enter the plain text: ")
            text = text.upper().replace(" ", "")
            print("\nPlain text: ", text)
            print("Cipher text: ", CaesarCipher.encrypt(text, key))
        elif choice == 3:
            text = input("Enter the cipher text: ")
            text = text.upper().replace(" ", "")
            print("\nCipher text: ", text)
            print("Plain text: ", CaesarCipher.decrypt(text, key))
        elif choice ==  4:
            exit = True
        else:
            print("Invalid Input. Try Again!")

def printMapping(key):
    print("The mapping for the cipher with key = {0} is : ".format(key))
    for c in CaesarCipher.alphabet:
        print(" {0} = {1}".format(c,CaesarCipher.encrypt(c, key)))
    return

if __name__ == "__main__":
    main()