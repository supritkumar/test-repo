def run_rec(n):
    if n==0:
        return
    print(n)
    run_rec(n-1)

n=int(input("Enter a number: "))
run_rec(n)
print('completed')