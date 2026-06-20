def is_palindrome(n):
    rev = 0
    if n<0 and  (n%10==0 or n!=0):
        return False
    else:
        while n > rev :
            digit  = n%10
            rev = (rev*10)+digit
            n= n//10
        if n == rev:
            return True
        elif rev//10 == n:
            return True
        else:
            return False

print(is_palindrome(1325231))
        
