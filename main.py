from stats import count_words
from stats import char_count
from stats import char_sort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    args = len(sys.argv)
    if args != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    word_count = count_words(text)
    char_dict = char_count(text)
    sorted_dicts = char_sort(char_dict)
    list_of_chars = []
    for item in sorted_dicts:
        char = item["char"]
        num = item["num"]
        paired = f"{char}: {num}"
        if char.isalpha() == True:
            list_of_chars.append(paired)


    print(
        f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{"\n".join(list_of_chars)}
============= END ==============="""
        )

main()