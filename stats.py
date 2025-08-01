def count_words(book_contents):
    words = book_contents.split()
    counter = 0
    for word in words:
        counter += 1
    return f"{counter} words found in the document"


def count_characters(book_contents):
    book_contents = book_contents.lower()
    char_dict = {}
    for char in book_contents:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
