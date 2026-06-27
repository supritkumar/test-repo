"""
a=[1,2, [3,[6,7],4],5,[[11,15,89],67]]

make this as proper flatten list
As it is a deep nested so we will go with recursion
"""



def nested_list_flatten(a):
    l = []
    for i in a:
        if isinstance(i,list):
            l.extend(nested_list_flatten(i))
        else:
            l.append(i)
    
    return l

my_list=[1,2, [3,[6,7],4],5,[[11,15,89],67]]

print(nested_list_flatten(my_list))