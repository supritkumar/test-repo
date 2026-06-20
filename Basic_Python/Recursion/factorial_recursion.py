def factorial_of(n):
    if n==0:
        return 1
    else:
        return n*factorial_of(n-1)
    
num = int(input("Enter the number: "))
print(f"factorial of {num} is: " ,factorial_of(num))