def is_pangram(sentence):
    sentence = sentence.lower()
    just_letters = [char for char in sentence if char.isalpha()]
    just_unique = len(set(just_letters))

    return just_unique == 26