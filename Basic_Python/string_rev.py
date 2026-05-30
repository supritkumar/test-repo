def string_reverse(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev

input_string = input("Enter a string to reverse: ")
print("Reversed string:", string_reverse(input_string))