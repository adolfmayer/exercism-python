import string
VOWELS = "aeiou"

def translate(text):
    words = text.split()
    translated_words = []

    for word in words:
        if word.startswith(tuple(VOWELS) + ("xr","yt")):
            result = word + "ay"

        elif "qu" in word and not any(c in VOWELS for c in word[:word.find("qu")]):
            index = word.find("qu") + 2
            result =  word[index:] + word[:index] + "ay"

        elif "y" in word and word.find("y") > 0 and not any(c in VOWELS for c in word[:word.find("y")]):
            index = word.find("y")          
            result = word[index:] + word[:index] + "ay"
        
        else:
            split_index = 0
            for i, char in enumerate(word):
                if char in VOWELS:
                    split_index = i
                    break            
            result = word[split_index:] + word[:split_index] + "ay"

        translated_words.append(result)

    return " ".join(translated_words)