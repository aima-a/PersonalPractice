def even_list(in_list=None):    # If the parameter in_list is not provided when calling the even_list function, it will default to None
    '''This program takes a list of numbers and returns a new list containing only the even numbers'''
    if in_list is None:     # If no list is provided, the function takes user input for the list
        list1 = input('Enter a list of numbers separated only by a comma: ').split(',')
    else:
        list1 = in_list
    list2 = []
    try:
        for i in list1:
            if int(i) % 2 == 0:
                list2.append(int(i))
        print(f'Here is your new list: {list2}')
    except ValueError:  # Exception handling for errors
        print('Invalid input; try again. Only use integers and do not enter a comma at the end of your list.')

a = [13, 17, 16, 20, 32]
even_list(a)

'''Alternatively: list2 = [int(i) for i in list1 if int(i) % 2 == 0]'''
