#Program to prime numbers

def prime_numbers(x,y):
    prime_list=[] 
    if ((x > 1 ) and (y>1)):
      for val in range(x, y):
        if val > 1:
          for i in range(2, val):
            if (val % i) == 0:
              break
          else:
           # print(val, end=" ")
            prime_list.append(val)
      print("The Prime numbers in the between {0} and {1} are: {2}".format(x,y,prime_list))      
    else:
        print("Enter The values greater than 0 and 1")    
        
NUM1=int(input("Enter The Value1: "))
NUM2=int(input("Enter The Value2: "))
prime_numbers(NUM1,NUM2)

