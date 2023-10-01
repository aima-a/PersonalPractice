'''Write a program that takes a list of numbers and returns a new list containing the numbers in ascending order, without using the built-in sort() function.'''
def asc_order(num_list):
    '''Bubble sort program'''
    n = len(num_list)   #Stores number of numbers in num_list
    for i in range(n - 1):  #Iterates through num_list, excluding the last element
        for j in range(n - i - 1):  #Inner loop ensures that we are only comparing elements within the unsorted portion of the list
            if num_list[j] > num_list[j+1]: #Checks if the element at index j in the list num_list is greater than the element at the next index, j + 1, and needs to be swapped
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j] #Swaps the elements at indices j and j + 1 if out of order
    return print(num_list)
numbers = [4, 2, 7, 1, 9, 5]
asc_order(numbers)