import random
print("Rules of the game: \n"+"Rock smashes scissors and wins \n"+"Scissors cuts paper and wins \n"+
      "Paper wraps rock and wins \n")
u=0
s=0
i=1
chance=int(input("How many rounds do u wish to play: "))
while i<=chance:
    print("Enter 1 for Rock\n Enter 2 for Paper\n Enter 3 for Scissors\n")
    ch=int(input("Enter your choice: "))
    while ch>3 or ch<1:
        ch=int(input("Enter a valid choice : "))
        
    if ch==1:
        cname='Rock'
    elif ch==2:
        cname='Paper'
    else:
        cname='Scissors'
        
    print ("Your choice is: ",cname )
    print("It's now the system's turn...")
    
    sysc = random.randint(1,3)
    while sysc == ch:
        sysc=random.randint(1,3)
        
    if sysc ==1:
        sysname = 'Rock'
    elif sysc ==2:
        sysname ='Paper'
    else:
        sysname = 'Scissors'
    
    print("Computer's choice is: ",sysname)
    print(cname, 'Vs ',sysname)
    
    if ch==sysc:
        print("It's a Tie",end="")
       
    if(ch==1 and sysc ==2):
        print("Paper wins over rock \nyou missed\n")
        s=s+1
    elif(ch==2 and sysc==1):
        print("Paper wins over rock \nyou won\n")
        u=u+1
    
    if(ch==1 and sysc==3):
        print("Rock wins over Scissors \nyou won\n")
        u=u+1
        
    elif(ch==3 and sysc==1):
        print("Rock wins over Scissors \nyou missed\n")
        s=s+1
    
    if(ch==2 and sysc==3):
        print("Scissors win over Paper \nyou missed\n")
        s=s+1
    elif(ch==3 and sysc==2):
        print("Scissors win over Paper \nyou won\n")
        u=u+1
        
    i+=1
    
print("Game over\n\n")
print("total score of user: ",u)
print("total score of system: ",s)
if u<s:
    print("You lose the game\n Better luck next time!")
elif u==s:
    print("It's a Draw! Play Again!")
else:
    print("Hurray!! You won!! ")
    
    