def pos_nu(x):
       NUM=[]
       NEG_NUM=[]
       for i in range(x):
           NUM.append(int(input("Enter the value: ")))
       print(NUM)
       for i in NUM:
           if (i <0):
               NEG_NUM.append(i)
       NEG_NUM.sort()
       print(NEG_NUM)
pos_nu(int(input("Enter The no of values to be stored:")))

#Enter The no of values to be stored:5
#Enter the value: -1
#Enter the value: -4
#Enter the value: 5
#Enter the value: 6
#Enter the value: -3
#[-1, -4, 5, 6, -3]
#[-4, -3, -1]
