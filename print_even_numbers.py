def even_num(x):
    EVEN_NUM=[]
    for i in range(1,x+1):
        if (i % 2 ==0):
           EVEN_NUM.append(i)
    print("The Even Numbers: ",EVEN_NUM)

even_num(int(input("Enter the value to print even numbers within it:")))


#Enter the value to print even numbers within it:50
#The Even Numbers:  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
