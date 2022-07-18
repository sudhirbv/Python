ARR=[]

def large_num():
    #for i in range(int(input("Enter the Num of values to be stored:"))):   #Method 1
    for i in range(1,int(input("Enter the Num of values to be stored:"))+1):  #Method 2
        ARR.append(int(input("Enter the value {0}:".format(i))))
    print(ARR)
    print("The Max value in the list is: ",max(ARR))

large_num()

#Method 1 output
#Enter the Num of values to be stored:5
#Enter the value 0:3
#Enter the value 1:6
#Enter the value 2:9
#Enter the value 3:10
#Enter the value 4:100
#[3, 6, 9, 10, 100]
#The Max value in the list is:  100


#Method 2 output
#Enter the Num of values to be stored:5
#Enter the value 1:3
#Enter the value 2:6
#Enter the value 3:9
#Enter the value 4:30
#Enter the value 5:50
#[3, 6, 9, 30, 50]
#The Max value in the list is:  50



#Different Method
# Python code
# To find the largest number in a list

##def maxelement(lst):
# displaying largest element
# one line solution
##print(max(lst))

# driver code
# input list
##lst = [20, 10, 20, 4, 100]
# the above input can also be given as
# lst = list(map(int, input().split())) # -> taking input from the user
##maxelement(lst)

