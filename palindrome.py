def palin(WORD1):
    WORD2=WORD1[::-1]
    if (WORD1 == WORD2):
        # return "Entered word is palindrome"
        print("Entered word is palindrome.")
        return
    else:
        print("Entered word is not palindrome.")
         #return "Entered word is not palindrome"
        return 
WORD1=input("Enter the word:")
palin(WORD1)
