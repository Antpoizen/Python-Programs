import hashlib
hashed = open("CRY100_04_Lab_hashes.txt","r")
allpossible = open("wordlist.txt","r")
solved = open("solved.txt","w")

for line in hashed:
    for x in allpossible:
        hashobj = hashlib.md5(x.encode())
        if hashobj != line:
            continue
        else:
            break
    crack = []
    crack.append(line + "" + hashobj + "\n")
            
for value in crack:   
    solved.write(crack[value])

hashed.close
allpossible.closed
solved.closed

exit



#mystring = input('Enter string to hash: ')
#hash_obj = hashlib.md5(mystring.encode())
#print(hash_obj.hexdigest())
