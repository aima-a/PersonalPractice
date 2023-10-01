'''Use list comprehensions to filter, transform, or perform calculations on lists. For example, create a list of squares
 of numbers from 1 to 10'''

squared_list = [x ** 2 for x in range(1, 11)]
print(squared_list)

squared_even_list = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(squared_even_list)

'''Nested list comprehension: flattening a list of lists into one'''
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in nested_list for num in sublist]
print(flattened_list)

'''Conditional list comprehension: filtering a list '''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
filtered_numbers = [num if num % 2 != 0 else num + 100 for num in numbers]
# This keeps odd numbers and adds 100 to the even numbers
print(filtered_numbers)

'''List comp. to zip two lists together with multiple iterables'''
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped_list = [(x, y) for x, y in zip(list1, list2)]
print(zipped_list)
