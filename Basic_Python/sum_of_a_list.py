def sum_of_a_list(list):
    sum=0
    for i in list:
        sum+=i
    return sum

n = int(input("Enter the number of elements in the list: "))
my_list =[]
for i in range(n):
    item=int(input(f"write element {i+1} : "))
    my_list.append(item)

print("the sum of ",n," items in the list is :", sum_of_a_list(my_list))
