from stats import count_words
from stats import count_characters
from stats import convert_dict_to_list
from pathlib import Path
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return

    book_path = sys.argv[1]

    if not Path(book_path).is_file():
        print(f"the path '{book_path}' is invalid, please recheck")
        sys.exit(1)
        return

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

    sys.exit(0)


main()
