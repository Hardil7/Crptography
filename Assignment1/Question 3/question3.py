from operator import itemgetter
import re,textwrap,numpy,string

fo = open('cipher1.txt')
word = fo.read()
fo.close()

def getfrequency(word):
	all_freq = {}   
	for i in word: 
		if i in all_freq: 
			all_freq[i] += 1
		else: 
			all_freq[i] = 1
	return re.findall('\d+',str(all_freq))

def frequency(word):
    result = [[x, 0.0] for x in UPcase]
    for x in word:
        result[x - ordinaryvalueof_A][1] += 1
    return result

def correlation(word):
    result = 0.0
    freq = frequency(word)
    freq.sort(key=itemgetter(1))

    for i, f in enumerate(freq):
        result += f[1] * outputs[i]
    return result
	
def calculateindex(y):
	n = len(y)
	freq = getfrequency(y)
	results = list(map(int, freq))
	results[:] = [x*(x-1) for x in results]
	numerator = sum(results)
	return  numerator/(n*(n-1))


new = ''.join(word)
new = textwrap.wrap(new, 1)
mat = numpy.array(new)
wow = mat.reshape((-1,5))
fin = wow.transpose()
new = numpy.ndarray.tolist(fin)
my_list5, my_list4, my_list3, my_list2, my_list1 = zip(new)
list1 = "".join(re.findall("[a-zA-Z]+", str(my_list1)))
list2 = "".join(re.findall("[a-zA-Z]+", str(my_list2)))
list3 = "".join(re.findall("[a-zA-Z]+", str(my_list3)))
list4 = "".join(re.findall("[a-zA-Z]+", str(my_list4)))
list5 = "".join(re.findall("[a-zA-Z]+", str(my_list5)))

print('\nconfidence Index of sentence1:' , calculateindex(list1))
print('\nconfidence Index of sentence2:', calculateindex(list2))
print('\nconfidence Index of sentence3:', calculateindex(list3))
print('\nconfidence Index of sentence4:', calculateindex(list4))
print('\nconfidence Index of sentence5:', calculateindex(list5))

print('\nHence, The key length is 5')


UPcase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
allcharachters = len(UPcase)
ordinaryvalueof_A = ord('A')
val1 = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228]
val2 = [0.02015,0.06094, 0.06966, 0.00153, 0.00772]
val3 = [0.04025, 0.02406, 0.06749,0.07507, 0.01929, 0.00095] 
val4 = [ 0.05987, 0.06327, 0.09056, 0.02758,0.00978, 0.02360, 0.00150, 0.01974, 0.00074]	
freq_val = val1 + val2 + val3 + val4
outputs = sorted(freq_val)
 
sorted_frequencies = [ord(x) for x in word.upper() if x.isupper()]
max_length = 0
max_mututal_coindcidence = -100.0      

for val in range(2, len(sorted_frequencies) // 20):
    sep = [[] for _ in range(val)]
    for j, x in enumerate(sorted_frequencies):
        sep[j % val].append(x)

    value_of_mutualcorrelation = -0.5*val + sum(correlation(p) for p in sep)

    if value_of_mutualcorrelation > max_mututal_coindcidence:
        max_length = val
        max_mututal_coindcidence = value_of_mutualcorrelation

sep = [[] for _ in range(max_length)]

for i, x in enumerate(sorted_frequencies):
    sep[i % max_length].append(x)

freqs = [frequency(p) for p in sep]

key = ""

print("\nEquation 1: k(0)")
print("Equation 2: k(1) = k(0) - 11")
print("Equation 3: k(2) = k(0) - 4")
print("Equation 4: k(3) = k(0) - 13")
print("Equation 5: k(4) = k(0) - 9\n")

for fre in freqs:
    fre.sort(key=itemgetter(1), reverse=True)
    a = 0
    maximum_coincidence = 0.0
    for y in range(allcharachters):
        cor = 0.0
        x = ordinaryvalueof_A + y
        for frc in fre:
            d = (ord(frc[0]) - x + allcharachters) % allcharachters
            cor += frc[1] * freq_val[d]
        if cor > maximum_coincidence:
            a = y
            maximum_coincidence = cor
    key += chr(a + ordinaryvalueof_A)


plaintext = (chr((x - ord(key[i % max_length]) + allcharachters) % allcharachters + ordinaryvalueof_A)
    for i, x in enumerate(sorted_frequencies))

decoded = " ".join(plaintext).lower()
print("Deciphered key is:", key)
print("\nPlainText:\n",decoded)


f= open("Decrypted Data.txt","w+")
f.write(decoded)
f.close
