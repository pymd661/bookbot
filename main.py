
from stats import *
import sys

print(f'Script name: {sys.argv[0]}')
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

else:
    
    # def get_book_text(filepath):
    #     with open(filepath) as f:
    #         file_contents = f.read()
    #         return file_contents

    def main():
        word_count = get_word_number(sys.argv[1])
        char_dict = get_char_count(sys.argv[1])
        list_count = list_of_dict(char_dict)
        list_count.sort(reverse=True, key=sort_on_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
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



