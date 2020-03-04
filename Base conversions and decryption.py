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

print ("       Welcome to Base conversions!")
while True:
    print ("")
    print ("-------------------------------------------")
    print ("What would you like to do?")
    print ("-Decimal to Binary:-----1")
    print ("-Decimal to Octal:------2")
    print ("-Decimal to Any Base:---3")
    print ("-Any Base to Decimal:---4")
    print ("-Encypt Word:-----------5")
    print ("-Decrypt Word:----------6")
    print ("Remember '!' will always kill the program.")
    print ("------------------------------------------- \n")
    choice = input ("")
    if choice == "!":
        break
    if choice == "1":
        # blank variable
        number=""
        #checks if input is a number
        while(not(number.isnumeric())):
            number = input("What is the decimal you want to convert to binary? \n")
        # takes the input and converts from string to integer
        tempnumb = int(number)
        #setting an empty variable so we can print a result
        bin_output = ""
        # while the integer is greater than 0 run
        while(tempnumb > 0):
            #does the math to conver the number into a binary number
            bin_output = str(tempnumb % 2) + bin_output
            tempnumb = int(tempnumb / 2)
        #prints the final result
        print (bin_output)   
        
    elif choice == "2":
        number=""
        while(not(number.isnumeric())):
            number = input("What is the decimal you want to convert to octal? \n")

        tempnumb = int(number) 
        bin_output = ""
        while(tempnumb > 0):
            bin_output = str(tempnumb % 8) + bin_output
            tempnumb = int(tempnumb / 8)

        print (bin_output)
    
    elif choice == "3":
        def reVal(num): 
            if (num >= 0 and num <= 9): 
                    return chr(num + ord('0')); 
            else: 
                    return chr(num - 10 + ord('A')); 

        def strev(str): 
            len = len(str); 
            for i in range(int(len / 2)): 
                    temp = str[i]; 
                    str[i] = str[len - i - 1]; 
                    str[len - i - 1] = temp; 

        def fromDeci(res, base, inputNum): 
                index = 0; 
                while (inputNum > 0): 
                    res+= reVal(inputNum % base); 
                    inputNum = int(inputNum / base); 
                res = res[::-1]; 
                return res; 
 
        inputNum = input("Select a decimal to be converted \n"); 
        base = input("Select a base for your decimal to be converted by. \n");
        inputNum = int(inputNum)
        base = int(base)
        res = ""; 
        print("Equivalent of", inputNum, "in base", 
                base, "is", fromDeci(res, base, inputNum)); # This code is contributed by mits https://www.geeksforgeeks.org/convert-base-decimal-vice-versa/
# with input modified to work for user input
    
    elif choice == "4":
        def val(c): 
                if c >= '0' and c <= '9': 
                        return ord(c) - ord('0') 
                else: 
                        return ord(c) - ord('A') + 10; 

        def toDeci(str,base): 
                llen = len(str) 
                power = 1 
                num = 0  
                for i in range(llen - 1, -1, -1): 
                        if val(str[i]) >= base: 
                                print('Invalid Number') 
                                return -1
                        num += val(str[i]) * power 
                        power = power * base 
                return num 
	
        strr = input("Please input a base number to be converted. \n")
        base = int(input("What base is that? \n"))
        print('Decimal equivalent of', strr, 
                                'in base', base, 'is', 
                                        toDeci(strr, base)) # This code is contributed by sahil shelangia https://www.geeksforgeeks.org/convert-base-decimal-vice-versa/
#modified to work for user inputs 

    elif choice == "5":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
        word = input("What is the word or phrase to encrypt? \n").upper()
        shift = int(input("How many places would you like to shift it? \n"))
        newletter = ""
        newword = ""
        for letter in word:
            newletter = alphabet[(alphabet.find(letter)+shift)%27]

            newword += newletter

        print (word+" = "+newword) 

    elif choice == "6":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
        word = input("What is the word or phrase to decrypt? \n").upper()
        shift = int(input("How many places is it shifted? \n"))
        newletter = ""
        newword = ""
        for letter in word:
            newletter = alphabet[(alphabet.find(letter)-shift)%27]


            newword += newletter

        print (word+" = "+newword)

    else:
        print("")
        print("-----------------------------")
        print("Please choose a valid option.")
        print("------------------------------")
        print("")
        

exit
