STR=""

def dup_str(STR):
       CHAR=list(STR.lower()) # Storing characters after converting to lower.
       #CHAR=list(STR) # Storing characters without converting.
       DUP={}
       for i in CHAR:
          if i in DUP:
              DUP[i]=DUP[i] + 1
          else:
              DUP[i]=1
          #print(DUP)
       print("The Occurence of characters in list: ",DUP)

dup_str(STR=input("Enter the string: "))
