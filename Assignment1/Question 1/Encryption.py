import sys
alphabet = " ABCDEFGHIJKLMNOPQESTUVWXYZ.,"
key =      "FPJVRKDWAEZ,BSGMTYICXQOLHU.N "

def encrypt(message):
    translated = ''

    for symbol in message:
        if symbol.upper() in alphabet:
            symIndex = alphabet.find(symbol.upper())
            if symbol.isupper():
                translated += key[symIndex].upper()
            else:
                translated += key[symIndex].lower()
        else:
            translated += symbol
    return translated

unencrypted_message = input("Enter your Message:")

f= open("Encrypted Data.txt","w+")

encrypted_message = encrypt(unencrypted_message)
f.write(encrypted_message)
f.close
print("PlainText: " + unencrypted_message)
print("Encrypted Message: " + encrypted_message)
