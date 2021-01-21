def getkey():
	key = ""
	f = open("Key.txt","r")
	for line in f:
		key += line.rstrip() 
		key = key + " "	
	key = key[:-1]
	key = key.split()
	f.close
	return key
	
def getencryptedmessage():
	f= open("Encrypted Data.txt","r")
	if f.mode == 'r':
		encrypted_message = f.read()
	f.close 
	return encrypted_message
	
key = getkey()
encrypted_message = getencryptedmessage()

print(key)		
print(encrypted_message)

no_of_blocks = int(len(encrypted_message)/len(key))
permutation_number = int(len(encrypted_message)/no_of_blocks)
print(no_of_blocks)


block = [encrypted_message[i:i+permutation_number] for i in range(0, len(encrypted_message), permutation_number)]
print(block)

plaintext = ""
for i in range(no_of_blocks):
	temp = str(block[i])
	
	for i in range(permutation_number):
		loc = int(key[i])
		plaintext += temp[loc]

print(plaintext)