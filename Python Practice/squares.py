'''Write a program that takes a list of numbers and returns the sum of the squares of the numbers.'''
def sum_of_squares(in_list=None):
    if in_list is None:
        num_list = input('Please enter a list of numbers (int or float) separated only by a comma: ').split(',')
    else:
        num_list = in_list
    try:
        squares = []
        sum = 0
        for i in num_list:
            squares.append(float(i)**2)
        for j in squares:
            sum += j
        return print(f'The sum of the squares of your numbers is {sum}.')
    except ValueError:
        return print('Invalid input; try again. No commas/spaces allowed at the beginning or end of your list.')
sum_of_squares()