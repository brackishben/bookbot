def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def char_count(text):
    lowered = text.lower()
    chars = {}
    for item in list(lowered):
        if item not in chars:
            chars[item] = 1
        else:
            chars[item] += 1
    return chars

def char_sort(char_dict):
    list_of_dicts = []
    for item in char_dict:
        num = char_dict[item]
        letter_dict = {}
        letter_dict["char"] = item
        letter_dict["num"] = num
        list_of_dicts.append(letter_dict)
    def sort_on(list_of_dicts):
        return list_of_dicts["num"]
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
