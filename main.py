from stats import count_words
from stats import count_characters


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_contents = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_contents)
    char_count = count_characters(book_contents)
    print(book_contents)
    print(num_words)
    print(char_count)


main()
