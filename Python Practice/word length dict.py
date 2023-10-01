'''Write a program that takes a list of words and returns a dictionary with the words as keys and their lengths as values.'''
def word_len_dict(in_list=None):
    if in_list is None:
        word_list = input('Enter a list of words separated by a space: ').split(' ')
    else:
        word_list = list(in_list)
    len_dict = {}
    try:
        for word in word_list:
            len_dict[word] = len(word)
        return print(f'Here is your dictionary with the words you entered and their lengths: {len_dict}')
    except ValueError:
        print('Invalid input. Try again.')
word_len_dict()