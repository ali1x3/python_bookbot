def count_words(book_contents):
    words = book_contents.split()
    counter = 0
    for word in words:
        counter += 1
    return counter


def count_characters(book_contents):
    book_contents = book_contents.lower()
    char_dict = {}
    for char in book_contents:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_on(dict):
    return dict["count"]


def convert_dict_to_list(char_dict):
    new_list = []
    for char in char_dict:
        if not char.isalpha():
            continue

        temp_dict = {}
        temp_dict["char"] = char
        temp_dict["count"] = char_dict[char]
        new_list.append(temp_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list
