def LEN_LIST(x):
    LST_ARY=[]
    count=0
  #  if(x>0):
    for i in range(x):
        #INP=int(input("Enter the value {0}: ".format(i)))  ## To allow only integers
        INP=(input("Enter the value {0}: ".format(i)))    ## To allow both words and integers
        LST_ARY.append(INP)
    print("The values of list is:", LST_ARY)
    for i in LST_ARY[::]:
          count=count + 1
    print("The lenght of list is:", count)
    
NUM=int(input("Enter the number of values to be stored in array:"))   #No of values to be stored in the array
LEN_LIST(NUM)
    


#Sample
#Enter the number of values to be stored in array:6
#Enter the value 0: 1
#Enter the value 1: 4
#Enter the value 2: 6
#Enter the value 3: 8
#Enter the value 4: 9
#Enter the value 5: 3
#The values of list is: [1, 4, 6, 8, 9, 3]
#The lenght of list is: 6
