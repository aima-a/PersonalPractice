def palindrome_checker(string=None):
    '''This function checks if a given string is a palindrome'''
    if string is None:
        my_string = input('Enter a string: ')
    else:
        my_string = string
    if my_string[::-1] == my_string:
        print('This is a palindrome')
    else:
        print('This is not a palindrome')


palindrome_checker()
