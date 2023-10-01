'''Write a program that takes a list of numbers and returns the product of all the numbers in the list.'''
def product_of_nums_in_list(list):
    product = 1
    for i in list:
        product *= i
    return print(product)
numbers = [4, 2, 7, 1, 9, 5]
product_of_nums_in_list(numbers)