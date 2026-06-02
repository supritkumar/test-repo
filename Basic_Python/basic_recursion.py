"""
Write a recursion function , take count from zero and as soon as it reach 500 with count , then exit the loop
"""

def basic_rec(count):
    if count == 500:
        return 0
    else:
        print("Hello World! ", count)
        basic_rec(count+1)

count = 0
basic_rec(count)