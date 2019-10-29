# Transposition Cipher

# Original: This_is_a_secret_message_ that_I_want_to_transmit
# encrypeted:hsi_ertmsaeta_att)rnmtti_sasce_esg)htiwn_otasi

def scramble2Encrypt(plaintext):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plaintext:
        if charCount % 2 == 0:
            evenChars = evenChars+ ch
        else:
            oddChars = oddChars = ch
        charCount = charCount + 1
    cipherText =  oddChars + evenChars
    return cipherText