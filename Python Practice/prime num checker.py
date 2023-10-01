'''Write a function to generate a list of prime numbers within a specified range.'''
def prime_checker(i):
    if i <= 1:
        return False
    elif i == 2 or i == 3:
        return True
    elif i % 2 == 0 or i % 3 == 0:
        return False
    else:
        for n in range(5, i + 2, 6):
            if i % n == 0 or i % (n + 2) == 0:
                return False
            else:
                return True

def prime_num_generator():
    start = int(input('Enter an integer as the starting point for your range of prime numbers: '))
    end = int(input('Enter an integer as the ending point for your range of prime numbers: '))
    prime_list = []
    for num in range(start, end + 1):
        if prime_checker(num) == True:
            prime_list.append(num)
    return print(prime_list)


prime_num_generator()
