
import os
def magic(Key,order):# this is creating the blocks
    dictionary= {}
    temp_list = []
    wordlist = []
    for lets in range(0,len(Key)): 
        wordlist.append(Key[lets])
        
    for x in range(0,len(Key)):
        char = Key[x] 
        if(Key.count(char) > 1):
            dictionary[char] = Key.count(char) 
    for y in range(0,len(order)):  
        ch = order[y]
        if((ch in dictionary.keys()) == True): 
            index = wordlist.index(ch) + 1
            tuple=(ch,index,(y + 1))
            temp_list.append(tuple)
            order[y] = "."
            wordlist[index - 1] = "." 
        elif((ch in dictionary.keys()) == False): 
            tuple=(ch,(Key.index(ch) + 1),(order.index(ch) + 1))
            temp_list.append(tuple)
    return temp_list 

def validate(option): # this checks the users input to see what definition needs to be run
    try: 
        try_int = int(option)
        if(try_int == 1):
            Start_Encryption_Process()
        elif(try_int == 2):
            Start_Decryption_Process()
        else:
            main()
    except:
        main()
        
def main(): # this is the ui that the user picks what option they want to do
    os.system('cls')  
    print("Encrypt [1]")
    print("Decrypt [2]\n")
    option = input("Option: ")
    validate(option)
    
def Start_Encryption_Process():# here is where the encryption starts
    os.system('cls')
    print("-----------------------------------Encryption-----------------------------------\n")
    word=input("Key: ")
    plaintext=input("\nPlaintext: ")
    keylen = len(word)
    s = sorted(word)
    smart_list = magic(word,s)
    grab_listy = alphabetize(smart_list)
    encrypted = encrypt(word,keylen,plaintext,grab_listy)
    os.system('cls')
    print("Key: " + str(word) + "\nCiphertext: " + encrypted)
    
def Start_Decryption_Process(): # here we are decrypting based off of the cipher text and and a key
    os.system('cls')
    print("-----------------------------------Decryption-----------------------------------\n")
    ciphertext=input("Ciphertext: ")
    word=input("\nKey: ")
    decrypt_block = [""]*len(word)
    decrypt_string = ""
    keylen=len(word)
    s=sorted(word)
    smart_list = magic(word,s)
    grab_listy = alphabetize(smart_list)
    divide = [ciphertext[i:i+keylen] for i in range(0,len(ciphertext),keylen)] 
    last_chunk = divide[(len(divide) -1)]
    size_last_chunk = len(last_chunk)
    add = (keylen - size_last_chunk)
    divide[(len(divide) - 1)] += ('X'*add)
    for item in range(0,len(divide)):
        block = divide[item]
        for x in range(0,len(word)):
            decrypt_block[grab_listy[x] - 1] = block[x]
        for y in range(0,len(decrypt_block)):
            current_letter = decrypt_block[y]
            decrypt_string += current_letter
    print(decrypt_string)
    
def alphabetize(smart_list): # this alphabatizes the our list so that we can do the permutation
    listy = []
    count = 1
    while(count < len(smart_list) + 1):
        for x in range(0,len(smart_list)):
            z = smart_list[x][1]
            if(z == count):
                listy.append(smart_list[x][2])
                count = count + 1
     
            elif(z != count):
                continue
    return listy

def encrypt(word,keylen,plaintext,listy): # this is the bulk of actual encryption
    encrypt_block = [""]*len(word)
    encrypted_string = ""
    divide = [plaintext[i:i+keylen] for i in range(0,len(plaintext),keylen)]
    last_chunk = divide[(len(divide) -1)]
    size_last_chunk = len(last_chunk)
    add = (keylen - size_last_chunk)
    divide[(len(divide) - 1)] += ('X'*add)
    for free in range(0,len(divide)):
        block = divide[free]
        for x in range(0,len(listy)):
            number = x
            idex = listy.index(number+1)
            encrypt_block[idex] = block[number]
        for let in range(0,len(encrypt_block)):
            current_block = encrypt_block[let]
            for numchars in range(0,len(current_block)):
                encrypted_string += current_block[numchars]
                
    return encrypted_string

if __name__ == '__main__':
    main()
