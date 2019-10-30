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






# write a caesarEncrypt(plainText, shift)
# write a caesarDecrypt(cipherText, shift)