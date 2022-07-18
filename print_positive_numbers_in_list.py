def pos_nu(x):
       NUM=[]
       POS_NUM=[]
       for i in range(x):
           NUM.append(int(input("Enter the value: ")))
       print(NUM)
       for i in NUM:
           if (i >=0):
               POS_NUM.append(i)
       print(POS_NUM)
pos_nu(int(input("Enter The no of values to be stored:")))

#Sample output:
#Enter The no of values to be stored:7
#Enter the value: 0
#Enter the value: -1
#Enter the value: -10
#Enter the value: 4
#Enter the value: -3
#Enter the value: 2
#Enter the value: -6
#[0, -1, -10, 4, -3, 2, -6]
#[0, 4, 2]
