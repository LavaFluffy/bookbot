from stats import get_num_words
from stats import get_character_summary
from stats import sort_char_summary
import sys

def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = "./books/frankenstein.txt"
    file_contents = get_book_text(path)
    print(file_contents)


if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    file_contents = get_book_text(path)
    num_words = get_num_words(file_contents)
    # print(f"{num_words} words found in the document")
    char_summary = get_character_summary(file_contents)
    # print(char_summary)
    sorted_char_summary = sort_char_summary(char_summary)
    # print(sorted_char_summary)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")

for entry in sorted_char_summary:
    if entry["char"] == " ":
        continue
    print(f"{entry["char"]}: {entry["num"]}")

print("============= END ===============")