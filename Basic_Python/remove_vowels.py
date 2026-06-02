def remove_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = ''
    for i in input_string:
        if i not in vowels:
            result = result+i
        else:
            pass
            
    return result

input_string = input("Enter a string to remove vowels: ")
print("String after removing vowels:", remove_vowels(input_string))