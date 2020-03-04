# ▄▄▄       ███▄    █ ▄▄▄█████▓ ██▓███   ▒█████   ██▓  ██████ ▓█████  ███▄    █ 
#▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒▓██░  ██▒▒██▒  ██▒▓██▒▒██    ▒ ▓█   ▀  ██ ▀█   █ 
#▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░▓██░ ██▓▒▒██░  ██▒▒██▒░ ▓██▄   ▒███   ▓██  ▀█ ██▒
#░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██▄█▓▒ ▒▒██   ██░░██░  ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒
# ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ ▒██▒ ░  ░░ ████▓▒░░██░▒██████▒▒░▒████▒▒██░   ▓██░
# ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   ▒▓▒░ ░  ░░ ▒░▒░▒░ ░▓  ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒ 
#  ▒   ▒▒ ░░ ░░   ░ ▒░    ░    ░▒ ░       ░ ▒ ▒░  ▒ ░░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░
#  ░   ▒      ░   ░ ░   ░      ░░       ░ ░ ░ ▒   ▒ ░░  ░  ░     ░      ░   ░ ░ 
#      ░  ░         ░                       ░ ░   ░        ░     ░  ░         ░ 
# 
from collections import Counter

print ("       Welcome to Encyptions and Decryptions!")
while True:
    print ("")
    print ("-------------------------------------------")
    print ("What would you like to do?")
    print ("Encrypt using Rotation Cipher:--1")
    print ("Decrypt using Rotation Cipher:--2")
    print ("Frequency Analysis:-------------3")
    print ("Remember '!' will always kill the program.")
    print ("------------------------------------------- \n")
    choice = input ("")
    if choice == "!":
            break
    elif choice == "1":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        word = input("What is the word or phrase to encrypt? \n").upper()
        shift = int(input("How many places would you like to shift it? \n"))
        newletter = ""
        newword = ""
        for letter in word:
            if letter not in alphabet:
                newword += str(" ")
                continue
            newletter = alphabet[(alphabet.find(letter)+shift)%26]

            newword += newletter

        print (word+" = "+newword) 

    elif choice == "2":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        word = input("What is the word or phrase to decrypt? \n").upper()
        shift = int(input("How many places is it shifted? \n"))
        newletter = ""
        newword = ""
        for letter in word:
            if letter not in alphabet:
                newword += str(" ")
                continue
            newletter = alphabet[(alphabet.find(letter)-shift)%26]


            newword += newletter

        print (word+" = "+newword)

    elif choice == "3":
        word = input("What is the word, phrase or book to count? \n").upper()
        word.split()
        str(word)
        def check_freq(wordlist):
            freq = {}
            for c in wordlist:
                freq[c] = wordlist.count(c)
            return freq
        print (check_freq(word))

    else:
        print ("")
        print ("-------------------")
        print ("")
        print ("-------------------")
        print ("")
exit
