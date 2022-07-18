ARR=[]

def smallest_num():
    #for i in range(int(input("Enter the Num of values to be stored:"))):   #Method 1
    for i in range(1,int(input("Enter the Num of values to be stored:"))+1):  #Method 2
        ARR.append(int(input("Enter the value {0}:".format(i))))
    print(ARR)
    print("The minimum value in the list is: ",min(ARR))

smallest_num()



