NUM=int(input("Enter The Value: "))
FACTORIAL=1
if(NUM > 0):
   for VAL in range(1,NUM+1):
      FACTORIAL=FACTORIAL * VAL
   #  VAL=VAL-1
   print("The Factorial of {0} is {1}".format(NUM,FACTORIAL))
else:
   print("Enter Positive value.")

