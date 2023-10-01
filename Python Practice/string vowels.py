def str_vowels(in_str=None):
    '''This program takes a string and returns the number of vowels in the string.'''
    if in_str is None:
        str = input('Enter a string: ')
    else:
        str = in_str
    vowel_count = 0
    vowels = ['a','e','i','o','u']
    str = str.lower()   # Makes the function case-insensitive
    for i in str:
        if i in vowels:
            vowel_count += 1
    print(f'The number of vowels in your string is: {vowel_count}')

str_vowels()

