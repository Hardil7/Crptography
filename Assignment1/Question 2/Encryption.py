import sys, random

def GenerateKey(m):
	key = [i for i in range(m)]
	print(key)
	random.shuffle(key)
	print(key)
	
	return key
	
m = int(input("Enter the permuatation Size:"))
key = GenerateKey(int(m))
encrypted_message = ""

# text editing
plaintext = input("Enter your Message:")
plaintext = plaintext.replace(" ","")
print(plaintext)
y = (m-(len(plaintext)%m))
if y != 0:
	y = len(plaintext) + (y)
plaintext = '{:$<{}s}'.format(plaintext, y)
print(plaintext)
#block generated
block = [plaintext[i:i+m] for i in range(0, len(plaintext), m)]
print(block)

#encryption on each block
for i in range(len(block)):
	temp = str(block[i])
	
	for i in range(m):
		loc = key.index(i)
		#loc = int(key[i])
		encrypted_message += temp[loc]
		
print(encrypted_message)


f= open("Encrypted Data.txt","w+")
f.write(encrypted_message)
f.close
with open('key.txt', 'w+') as f:
    for item in key:
        f.write("%s\n" % item)