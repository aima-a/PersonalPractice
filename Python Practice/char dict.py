'''Write a program that takes a string and returns a dictionary with the characters as keys and the number of occurrences of each character as values.'''
def char_dict(in_str=None):
    if in_str is None:
        str = input('Enter a string: ')
    else:
        str = in_str
    dict = {}
    unique_chars = set(str)
    for char in unique_chars:
        dict[char] = str.count(char)
    return print(dict)
char_dict()
