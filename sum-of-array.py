def sum_array(x):
    LST_ARY=[]
    sum=0
    if(x>0):
        for i in range(x):
            INP=int(input("Enter the value {0}: ".format(i)))
            LST_ARY.append(INP)
        for j in LST_ARY:
         sum=sum+int(j)
        print("Sum of array is :",sum)
    else:
        print("Enter Positive value.")
    
ARY=int(input("Enter the number of values to be stored in array:"))   #No of values to be stored in the array
sum_array(ARY)
    
    
