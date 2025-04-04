
from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    word_count = get_word_number(r"books/frankenstein.txt")
    char_dict = get_char_count(r"books/frankenstein.txt")
    print(f"{word_count} words found in the document")
    print(char_dict)

if __name__== "__main__":
    main()



