def sum_num(x):
       NUM=[]
       for i in range(x):
           NUM.append(int(input("Enter the value: ")))
       print(NUM)
       SUM=0
       for i in NUM:
           SUM=SUM + i
       print("The sum of list is: ",SUM)
sum_num(int(input("Enter The no of values to be stored:")))

"""
Sample output

Enter The no of values to be stored:5
Enter the value: 4
Enter the value: 7
Enter the value: 9
Enter the value: 13
Enter the value: 15
#[4, 7, 9, 13, 15]
The sum of list is:48

Enter The no of values to be stored:5
Enter the value: 3
Enter the value: 6
Enter the value: -1
Enter the value: 5
Enter the value: 60
#[3, 6, -1, 5, 60]
The sum of list is:  73

Other Method:

## Python program to find sum of elements in list
total = 0
## creating a list
list1 = [11, 5, 17, 18, 23]
## Iterate each element in list
## and add them in variable total
for ele in range(0, len(list1)):
    total = total + list1[ele]
## printing total value
print("Sum of all elements in given list: ", total)
"""
