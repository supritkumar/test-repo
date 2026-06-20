"""
take an example of recursion where print statement is there before and after the recursion call
"""

def rec_run(n):
    if n==0:
        return
    print(n)
    rec_run(n-1)    
    print(n)

num = int(input("enter the number : "))
rec_run(num)