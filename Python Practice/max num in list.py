def max_num_in_list(in_list=None):
    if in_list is None:
        list = input('Enter a list of numbers separated only by a comma: ').split(',')
    else:
        list = in_list
    max_num = max(list)
    return print(f'The highest number you entered is {max_num}')
numbers = [4, 2, 7, 1, 9, 5]
max_num_in_list(numbers)