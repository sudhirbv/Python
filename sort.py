def pos_nu(x):
       NUM=[]
       for i in range(x):
           NUM.append(int(input("Enter the value: ")))
       SORT_NUM = sorted(NUM)
       print(NUM)       
       print(SORT_NUM)
pos_nu(int(input("Enter The no of values to be stored:")))

#Sample Output:
#Enter The no of values to be stored:5
#Enter the value: -1
#Enter the value: 4
#Enter the value: -7
#Enter the value: 9
#Enter the value: -5
#[-1, 4, -7, 9, -5]
#[-7, -5, -1, 4, 9]
