from stats import count_words
from stats import count_characters
from stats import convert_dict_to_list


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    num_words = count_words(book_contents)
    char_dict = count_characters(book_contents)
    char_list = convert_dict_to_list(char_dict)
    # print(book_contents)
    # print(num_words)
    # print(char_dict)
    # print(char_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in char_list:
        print(f"{dict["char"]}: {dict["count"]}")
    print("============= END ===============")


main()
