def str_len_sorter(str_list):
    '''This program takes a list of strings and returns a new list containing the strings sorted by length from shortest
    to longest'''
    try:
        if len(str_list) < 2:
            return print('You need at least 2 strings in your list.')
        else:
            str_list.sort(key=lambda s:len(s)) #Lambda is a mapping function that returns the length of each string in the list
            return print(str_list)
    except ValueError:
        return print('Invalid inputs. Try again.')
strings = ['apple', 'banana', 'cherry', 'kiwi']
str_len_sorter(strings)


