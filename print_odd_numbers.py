def odd_num(x):
    ODD_NUM=[]
    EVEN_NUM=[]
    for i in range(1,x+1):
        if (i % 2 !=0):
           ODD_NUM.append(i)
        else:
           EVEN_NUM.append(i)
    print("The Odd Numbers: ",ODD_NUM)
    print("The Even Numbers: ",EVEN_NUM)

odd_num(int(input("Enter the value to print odd numbers within it:")))


#Enter the value to print odd numbers within it:60
#The Odd Numbers:  [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
#The Even Numbers:  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]
