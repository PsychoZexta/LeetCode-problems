def isPalindrome(x):
    check=x
    palindrome=0
    if x>=0 and x<10:
        return True
    if x<0 or(x%10==0):
        return False
    while(x!=0):
        remainder=x%10
        x=int(x/10)
        palindrome=(palindrome*10)+remainder
    if palindrome==check:
        return True
    else:
        return False
        
print(isPalindrome(0))