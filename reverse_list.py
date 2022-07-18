def REV_LIST(x):
    LST_ARY=[]
    if(x>0):
        for i in range(x):
            INP=int(input("Enter the value {0}: ".format(i)))
            LST_ARY.append(INP)
        REV_LIST=LST_ARY[::-1]
        print("Reverse of the input list is: ",REV_LIST)
    else:
        print("Enter Positive value.")
    
NUM=int(input("Enter the number of values to be stored in array:"))   #No of values to be stored in the array
REV_LIST(NUM)
    
    
# Sample Output:
#Enter the number of values to be stored in array:5
#Enter the value 0: 3
#Enter the value 1: 5
#Enter the value 2: 7
#Enter the value 3: 8
#Enter the value 4: 9
#Reverse of the input list is:  [9, 8, 7, 5, 3]
#
#

