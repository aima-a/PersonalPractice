'''Write a function to calculate the factorial of a given integer. For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1
= 120.'''
def factorial_calc(integer=None):
    factorial = 1
    if integer is None:
        num = int(input('Enter an integer: '))
    else:
        num = int(integer)
    for i in range(1, num + 1):
        factorial *= i
    return print(factorial)


factorial_calc(7.6)
