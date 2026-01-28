def is_isogram(string):
    string = string.lower()
    only_letters = [char for char in string if char.isalpha()]
    only_unique = len(set(only_letters))

    return only_unique == len(only_letters)