import random

#Scenarios
#rock + rock ==> Tie
#paper + paper ==> Tie
#scissor + scissor ==> Tie

#rock + scissor ==> rock
#paper + scissor ==> scissor 
#rock + paper  ===> paper


Li1 = ["rock","paper","scissor"]
COUNT={}
POINTS={}

def rock_paper_scissor(NO_GMS):
    print(type(NO_GMS))
    Tie = 0
    User = 0
    System = 0
    for i in range(NO_GMS):
        USR_INPT = input("Pick any one of the following rock, scissor, paper: ")
        if(USR_INPT in Li1 ):
            SYS_INPT = random.choice(Li1)
            print("System input is: ",SYS_INPT)
            if (USR_INPT == SYS_INPT):    # This will cover 1,2,3 scenarios
                print("Tie")
                Tie = Tie + 1
                if USR_INPT in COUNT:
                    COUNT[USR_INPT]+=1
                else:
                    COUNT[USR_INPT]=1
            elif (USR_INPT == "rock" and SYS_INPT == "scissor"):
                print("The Winner is User:", USR_INPT)
                User = User + 1
                if USR_INPT in COUNT:
                    COUNT[USR_INPT]+=1
                else:
                    COUNT[USR_INPT] = 1
            elif (USR_INPT == "scissor" and SYS_INPT == "paper"):
                print("The Winner is User:", USR_INPT)
                User = User + 1
                if USR_INPT in COUNT:
                    COUNT[USR_INPT]+=1
                else:
                    COUNT[USR_INPT] = 1
            elif (USR_INPT == "paper" and SYS_INPT == "rock"):
                print("The Winner is User:",USR_INPT)
                User = User + 1
                if USR_INPT in COUNT:
                    COUNT[USR_INPT]+=1

                else:
                    COUNT[USR_INPT] = 1
#System Portion
            elif (USR_INPT == "scissor" and SYS_INPT == "rock"):
                print("The Winner is System:", SYS_INPT)
                System = System + 1
                if SYS_INPT in COUNT:
                    COUNT[SYS_INPT]+=1
                else:
                    COUNT[USR_INPT] = 1
            elif (USR_INPT == "paper" and SYS_INPT == "scissor"):
                print("The Winner is System:", SYS_INPT)
                System = System + 1
                if SYS_INPT in COUNT:
                    COUNT[SYS_INPT]+=1
                else:
                    COUNT[USR_INPT] = 1
            elif (USR_INPT == "rock" and SYS_INPT == "paper"):
                print("The Winner is System:", SYS_INPT)
                System = System + 1
                if SYS_INPT in COUNT:
                    COUNT[SYS_INPT]+=1
                else:
                    COUNT[USR_INPT] = 1

        else:
            print("Entered Word is not in the list.")
           
    print(COUNT)
    print("The points summary of Tie: ", Tie)
    print("The points summary of User: ", User)
    print("The points summary of System: ", System)
    POINTS["Tie"]=Tie
    POINTS["User"]=User
    POINTS["System"]=System
    print(POINTS)
    WINNER = max(POINTS, key=POINTS.get )
   # WINNER = max(POINTS.values())

    if(User == System):
        print("Its a tie between User and System.")
    else: 
        print("The Winner is {0} with points: {1} ".format(WINNER,max(POINTS.values())))
    
rock_paper_scissor(NO_GMS = int(input("Enter Number of games you want to play: ")))




##################################################################
#Sample test case outputs:

#Case1:
#Enter Number of games you want to play: 6
#<class 'int'>
#Pick any one of the following rock, scissor, paper: rock
#System input is:  scissor
#The Winner is User: rock
#Pick any one of the following rock, scissor, paper: rock
#System input is:  paper
#The Winner is System: paper
#Pick any one of the following rock, scissor, paper: rock
#System input is:  paper
#The Winner is System: paper
#Pick any one of the following rock, scissor, paper: rock
#System input is:  scissor
#The Winner is User: rock
#Pick any one of the following rock, scissor, paper: paper
#System input is:  rock
#The Winner is User: paper
#Pick any one of the following rock, scissor, paper: scissor
#System input is:  rock
#The Winner is System: rock
#{'rock': 3, 'paper': 1}
#The points summary of Tie:  0
#The points summary of User:  3
#The points summary of System:  3
#{'Tie': 0, 'User': 3, 'System': 3}
#Its a tie between User and System.

#Case2:
#Enter Number of games you want to play: 5
#<class 'int'>
#Pick any one of the following rock, scissor, paper: rock
#System input is:  scissor
#The Winner is User: rock
#Pick any one of the following rock, scissor, paper: rock
#System input is:  paper
#The Winner is System: paper
#Pick any one of the following rock, scissor, paper: rock
#System input is:  paper
#The Winner is System: paper
#Pick any one of the following rock, scissor, paper: rock
#System input is:  scissor
#The Winner is User: rock
#Pick any one of the following rock, scissor, paper: paper
#System input is:  rock
#The Winner is User: paper
#Pick any one of the following rock, scissor, paper: scissor
#System input is:  rock
#The Winner is System: rock


##################################################################





