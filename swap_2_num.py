ARR=[]

def store_num():
    #for i in range(int(input("Enter the Num of values to be stored:"))):   #Method 1
    for i in range(1,int(input("Enter the Num of values to be stored:"))+1):  #Method 2
        ARR.append(int(input("Enter the value {0}:".format(i))))
    print("The list before swapping",ARR)
#    for i in ARR:
#        print(ARR.index[i])
    
    
    print("The minimum value in the list is: ",min(ARR))
#POS1=int(input("the postion 1 which need to be swapped:"))
#POS2=int(input("the postion 1 which need to be swapped:"))
def swap_num(ARR,POS1,POS2):
    ARR[POS1], ARR[POS2] = ARR[POS2], ARR[POS1]
    print("The list after swapping",ARR)

store_num()
swap_num(ARR,POS1=int(input("the posn 1 which need to be swapped posn2 :")),POS2=int(input("the posn 2 which need to be swapped pos1:")))


#Enter the Num of values to be stored:4
#Enter the value 1:30
#Enter the value 2:50
#Enter the value 3:60
#Enter the value 4:90
#The list before swapping [30, 50, 60, 90]
#The minimum value in the list is:  30
#the postion 1 which need to be swapped:1
#the postion 2 which need to be swapped:3
#The list after swapping [30, 90, 60, 50]
#
