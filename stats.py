def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    chars = {}
    for char in text:
        char = char.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sort_dict(chars_dict):
    new_list = []
    for chars in chars_dict:
        new_list.append({"name": chars, "num": chars_dict[chars]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list