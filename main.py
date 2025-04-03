
from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    num_words = word_number("books/frankenstein.txt")
    print (f"{num_words} words found in the document")

if __name__== "__main__":
    main()



