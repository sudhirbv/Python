def LEN_LIST(x):
    LST_ARY=[]
    for i in range(x):
        INP=int(input("Enter the value {0}: ".format(i)))  ## To allow only integers
        LST_ARY.append(INP)
    print("The values of list is:", LST_ARY)
    count=1
    for i in LST_ARY[::]:
          count=count * i
    print("The mutiples of list values is:", count)
    
NUM=int(input("Enter the number of values to be stored in array:"))   #No of values to be stored in the array
LEN_LIST(NUM)
    
