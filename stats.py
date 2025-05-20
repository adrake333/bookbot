def num_words(text):
    words = text.split()
    return len(words)

def num_characters(text):
    lower_text = text.lower()
    characters = {}
    for letter in lower_text:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters

def sort_on(character_count):
    return character_count["num"]

def pretty_report(character_count):
    character_list = []
    for key, value in character_count.items():
        if key.isalpha():
            character_list.append({"char": key, "num": value})
    character_list.sort(reverse=True, key=sort_on)
    return character_list
