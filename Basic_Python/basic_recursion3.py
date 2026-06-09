def run_rec(n):
    if n==0:
        return
    run_rec(n-1)
    print(n)

n=int(input("Enter a number: "))
run_rec(n)
print('completed')