# Transposition Cipher

# Original: This_is_a_secret_message_ that_I_want_to_transmit
# encrypeted:hsi_ertmsaeta_att_rnmtti_sasce_esg_htiwn_otasi

def scramble2Encrypt(plaintext):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plaintext:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

def scramble2Decrypt(ciphertext):
    halfLength = len(ciphertext) // 2
    evenChars= ciphertext[halfLength:]
    oddChars = ciphertext[:halfLength]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText

def encryptMessage():
    msg = input("Enter the message to encrypt: ")
    cipherText = scramble2Encrypt(msg)
    print("The message is:", cipherText)

# write a stripSpaces(text) function here

def stripSpaces(text):
    print(text.replace(" ", ""))
print(stripSpaces("Hello my name is John"))


# write a caesarEncrypt(plainText, shift)
def caesarEncrypt(plainText, shift):
    result = ""
    for i in range(len(plainText)):
        char = plainText[i]
        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
        return result

plainText = "Hello"
shift = 4

print("Text: " + plainText)
print("Shift pattern: " + str(shift))
print("Cipher: " + caesarEncrypt(plainText, shift))

# write a caesarDecrypt(cipherText, shift)


