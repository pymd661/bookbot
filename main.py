
from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    word_count = get_word_number(r"books/frankenstein.txt")
    char_dict = get_char_count(r"books/frankenstein.txt")
    list_count = list_of_dict(char_dict)
    list_count.sort(reverse=True, key=sort_on_count)
    # print(f"{word_count} words found in the document")
    # print(char_dict)
    # def print_report():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in list_count:
        if dict['letter'].isalpha():
            print(f"{dict['letter']}: {dict['count']}")
        else:
            pass
    print("============= END ===============")


if __name__== "__main__":
    main()



