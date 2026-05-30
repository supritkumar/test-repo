"""
write a python program to count the number of characters in a string
sample : google.com
Expected result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

"""

s = str(input("sample : "))

def character_frequency(a):
    myset = set(a)
    mydict = {}

    for i in myset:
        count = 0
        for j in a:
            if i==j:
                count+=1
            else:
                pass
        mydict[i] = count
    return mydict

print("Expected Result : ", character_frequency(s))