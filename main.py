from stats import get_num_words, get_num_chars
import sys

if len(sys.argv) > 1:
    book_path = sys.argv[1]
    get_num_words(book_path)
    get_num_chars(book_path)
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
