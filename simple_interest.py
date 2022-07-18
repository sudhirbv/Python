def SI_interest(p,t,r):
    if(NUM1 > 0 and NUM2 > 0 and NUM3 > 0):
      si=(p*t*r)/100
      print("Simple interest is: ",si)
    else:
        print("enter values greater than 0")
           
NUM1=int(input("Enter The Principle: "))
NUM2=int(input("Enter The Time: "))
NUM3=int(input("Enter The Interest: "))
SI_interest(NUM1,NUM2,NUM3)    
