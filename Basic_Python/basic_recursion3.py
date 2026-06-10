def run_rec(n):
    if n==0:
        return
    run_rec(n-1)
    print(n)  #This statement will run when one base condition will meet and it will go to previous function control one by one. After run_rec(0) complete, it will go to run_rec(1) and will execute next further lines after this, after completing run_rec(1). Now will go to previous run_rec(2) and same again run_rec(3) and will complete all the executable code after function call.

n=int(input("Enter a number: "))
run_rec(n)
print('completed')