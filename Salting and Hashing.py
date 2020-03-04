import hashlib
import random

salted = ""
salt = []
salte = []
saltede = ""
mystring = input('Enter string to hash: ')
print (mystring)

for w in range(0,(len(mystring)*2)):
    randomletters = random.randrange(32,126)
    orde = chr(randomletters)
    salt.append(orde)
    
for x in salt:
    salted += x

for y in range(0,(len(mystring)*2)):
    randomletterse = random.randrange(32,126)
    ordee = chr(randomletterse)
    salte.append(ordee)
    
for z in salte:
    saltede += z
    
mystring = (saltede + mystring + salted)

print ("This is the Salt: Before the word > " + saltede + " | " + salted + " < End of word \n")
print ("This is the String before the Hash: " + mystring + "\n")
hash_obj = hashlib.md5(mystring.encode())
print("This is the Salted Hash: " + hash_obj.hexdigest())
