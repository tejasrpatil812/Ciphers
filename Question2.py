import CaesarCipher
charFrequency={'A':0.080,
                'B':0.015,
                'C':0.030,
                'D':0.040,
                'E':0.130,
                'F':0.020,
                'G':0.015,
                'H':0.060,
                'I':0.065,
                'J':0.005,
                'K':0.005,
                'L':0.035,
                'M':0.030,
                'N':0.070,
                'O':0.080,
                'P':0.020,
                'Q':0.002,
                'R':0.065,
                'S':0.060,
                'T':0.090,
                'U':0.030,
                'V':0.010,
                'W':0.015,
                'X':0.005,
                'Y':0.020,
                'Z':0.082}

'''
    Cipher text to test -
        XTKYBFWJXJHZWNYD
        KCECMKS
'''
def main():
    ciphertext = input("Enter the cipher text: ")
    decipher(ciphertext.upper())

def decipher(ciphertext):
    frequencyMap = calculateFrequency(ciphertext)
    print("Frequency of each letter in {0} is: ". format(ciphertext))
    print(frequencyMap)

    qMap = dict()
    for i in range(26):
        q = 0
        for c in frequencyMap.keys():
            cypherAlphabet = CaesarCipher.decrypt(c, i)
            q = q + frequencyMap[c] * charFrequency[cypherAlphabet];
        qMap[i] = q

    #sort according to values
    qMap = {k: v for k, v in sorted(qMap.items(), key=lambda item: item[1],reverse=True)}
    print("Most probable keys are (Top 5)- ")
    count = 5
    for i in qMap.keys():
        count = count - 1
        print("i = {0} q = {1}".format(i, qMap.get(i)))
        plainText = ""
        for c in ciphertext:
            cypherAlphabet = CaesarCipher.decrypt(c,i)
            plainText += cypherAlphabet

        print("Plain Text = " + plainText)
        if count == 0:
            break
        
    return

def calculateFrequency(text):
    frequencyMap = dict()

    #count occurence of letters
    for c in text:
        val = frequencyMap.get(c, 0)
        frequencyMap[c] = val+1

    #convert to frequency
    for c in frequencyMap.keys():
        val = frequencyMap[c] / len(text)
        frequencyMap[c] = val

    return frequencyMap


if __name__ == "__main__":
    main()