def translate(text):
    consonants = ("b","c","d","f","g","h","j","k","l","m",
                  "n","p","q","r","s","t","v","w","x","y","z")
    vowels = ("a","e","i","o","u")

    words = text.split()
    translated_words = []

    for word in words:
        if word.startswith(vowels + ("xr","yt")):
            translated_words.append(word + "ay")
            continue

        if "qu" in word:
            index = word.find("qu")
            cut = word[:index]
            if not any(c in vowels for c in cut):
                translated_words.append(word[index+2:] + cut + "qu" + "ay")
                continue

        if "y" in word:
            index = word.find("y")
            if index != 0:
                cut = word[:index]
                if not any(c in vowels for c in cut):
                    translated_words.append(word[index:] + cut + "ay")
                    continue

        count = 0
        for i, char in enumerate(word):
            if char in consonants or i == 0:
                count += 1
            else:
                break

        if count == 0:
            translated_words.append(word + "ay")
        else:
            translated_words.append(word[count:] + word[:count] + "ay")

    return " ".join(translated_words)

    
   