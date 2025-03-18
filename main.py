import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    char_dict = get_num_characters(text)
    sorted_chars = sort_dict(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")

if __name__ == "__main__":
    main()