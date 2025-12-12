def get_num_words(book_path):
    """Reads the text from a book file and counts words."""
    with open(book_path) as f:
        num_words = len(f.read().split())
    print(f"Found {num_words} total words")


def get_num_chars(book_path):
    """Reads the text from a book file and counts characters."""
    char_dic = []
    with open(book_path) as f:
        content = f.read().lower()
        for char in "abcdefghijklmnopqrstuvwxyz":
            char_dic.append({"char": char, "num": content.count(char)})
    char_dic.sort(
        key=lambda x: x["num"], reverse=True
    )  # lambda x: x["num"] is like def f(x): return x["num"]
    for item in char_dic:
        print(f"{item['char']}: {item['num']}")
    # print(char_dic)
