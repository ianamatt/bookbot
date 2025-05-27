import sys

from stats import (
    get_num_words, 
    get_num_chars, 
    sort_dict)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_dict = sort_dict(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_dict:
        if char["name"].isalpha():
            print(f"{char["name"]}: {char["num"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()