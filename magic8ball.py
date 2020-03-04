import random
print ("  Welcome to Magic 8-Ball!  ")
print ("--! will kill the program.--")
print ("")
while True:
    yor = input ("Ask a question.\n")
    if yor == "!":
        break
    else:
        choices=("It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely.","You may rely on it.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful.") 
        value = random.randint(0,len(choices)-1) 

        print(choices[value])
        print ("------------------------")
        print ("")
exit
