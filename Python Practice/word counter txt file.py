import re
import string
def word_counter():
    '''This function reads a text file and counts the frequency of each word in it'''
    try:
        file_path = input('Enter the file path to your .txt file: ')
        with open(file_path, 'r') as file:  # Opens file
            contents = file.read()  # Reads text from file
            delimiter_pattern = r'[ \.\!,\n]+'
            words = re.split(delimiter_pattern, contents)
            word_count_dict = {}
            for word in words:
                if word:    # Ensures empty strings are not counted
                    word = word.strip(string.punctuation + ')').lower()
                    if word not in word_count_dict:
                        word_count_dict[word] = 1
                    else:
                        word_count_dict[word] += 1
        return word_count_dict
    except FileNotFoundError or PermissionError:
        return 'File not found or permission error. Try again.'
print(word_counter())
