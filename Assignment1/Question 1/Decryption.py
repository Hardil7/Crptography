import sys

alphabet = " ABCDEFGHIJKLMNOPQESTUVWXYZ.,"
key =      "FPJVRKDWAEZ,BSGMTYICXQOLHU.N "

def decrypt(message):
    translated = ''

    for symbol in message:
        if symbol.upper() in key:
            symIndex = key.find(symbol.upper())
            if symbol.isupper():
                translated += alphabet[symIndex].upper()
            else:
                translated += alphabet[symIndex].lower()
        else:
            translated += symbol
    return translated
  

f= open("Encrypted Data.txt","r")
if f.mode == 'r':
    encrypted_message = f.read()
decrypted_message = decrypt(encrypted_message)

print("Decrypted Message: " + decrypted_message)

f.close
